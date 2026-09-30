from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import RegisterForm, ResumeUploadForm
from .models import ResumeAnalysis
from .services import extract_pdf_text, detect_skills, analyze_match

def dashboard(request):
    analyses = ResumeAnalysis.objects.filter(user=request.user) if request.user.is_authenticated else []
    return render(request, "dashboard.html", {"analyses": analyses})

def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Account created successfully.")
        return redirect("dashboard")
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        messages.error(request, "Invalid username or password.")
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def analyze_resume(request):
    if request.method != "POST":
        return redirect("dashboard")

    form = ResumeUploadForm(request.POST, request.FILES)
    if form.is_valid():
        analysis = form.save(commit=False)
        analysis.user = request.user
        text = extract_pdf_text(request.FILES["resume"])
        found = detect_skills(text)
        score, missing, _ = analyze_match(found, analysis.job_role)

        analysis.detected_skills = found
        analysis.missing_skills = missing
        analysis.match_score = score
        analysis.extracted_text = text[:15000]
        analysis.save()

        return render(request, "result.html", {
            "analysis": analysis,
            "skills": found,
            "missing": missing,
        })

    messages.error(request, "Please correct the upload form.")
    return render(request, "dashboard.html", {
        "form": form,
        "analyses": ResumeAnalysis.objects.filter(user=request.user),
    })
