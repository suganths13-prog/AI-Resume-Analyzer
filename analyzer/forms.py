from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ResumeAnalysis

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = ResumeAnalysis
        fields = ("resume", "job_role")
        widgets = {
            "job_role": forms.Select(
                choices=[
                    ("Python Developer", "Python Developer"),
                    ("Django Developer", "Django Developer"),
                    ("Java Developer", "Java Developer"),
                    ("Data Analyst", "Data Analyst"),
                    ("Software Developer", "Software Developer"),
                    ("Frontend Developer", "Frontend Developer"),
                ]
            )
        }

    def clean_resume(self):
        resume = self.cleaned_data["resume"]
        if not resume.name.lower().endswith(".pdf"):
            raise forms.ValidationError("Please upload a PDF resume.")
        if resume.size > 5 * 1024 * 1024:
            raise forms.ValidationError("PDF must be smaller than 5 MB.")
        return resume
