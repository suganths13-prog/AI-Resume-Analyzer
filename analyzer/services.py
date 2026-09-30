import re
import fitz

SKILLS = [
    "python", "java", "c", "c++", "c#", "javascript", "typescript",
    "html", "css", "react", "angular", "vue", "django", "flask",
    "fastapi", "node.js", "sql", "mysql", "postgresql", "mongodb",
    "git", "github", "docker", "aws", "azure", "linux", "rest api",
    "machine learning", "deep learning", "pandas", "numpy", "scikit-learn",
    "tensorflow", "power bi", "excel", "tableau", "data analysis",
    "communication", "problem solving", "data structures", "algorithms"
]

ROLE_SKILLS = {
    "Python Developer": ["python", "sql", "git", "django", "rest api", "data structures"],
    "Django Developer": ["python", "django", "html", "css", "javascript", "sql", "git"],
    "Java Developer": ["java", "sql", "git", "data structures", "algorithms", "rest api"],
    "Data Analyst": ["python", "sql", "excel", "power bi", "pandas", "numpy", "data analysis"],
    "Software Developer": ["python", "java", "sql", "git", "data structures", "algorithms"],
    "Frontend Developer": ["html", "css", "javascript", "react", "git"],
}

def extract_pdf_text(uploaded_file):
    data = uploaded_file.read()
    doc = fitz.open(stream=data, filetype="pdf")
    text = "\n".join(page.get_text() for page in doc)
    doc.close()
    uploaded_file.seek(0)
    return text

def detect_skills(text):
    lower = text.lower()
    found = []
    for skill in SKILLS:
        pattern = r"(?<![a-z0-9])" + re.escape(skill) + r"(?![a-z0-9])"
        if re.search(pattern, lower):
            found.append(skill)
    return sorted(set(found))

def analyze_match(found_skills, job_role):
    required = ROLE_SKILLS.get(job_role, [])
    found_set = set(found_skills)
    missing = [skill for skill in required if skill not in found_set]
    score = round((len(required) - len(missing)) / len(required) * 100) if required else 0
    return score, missing, required
