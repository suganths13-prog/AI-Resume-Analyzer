# AI Resume Analyzer

A beginner-friendly Django project that lets users upload a resume PDF, extracts the text, detects common skills, and compares the resume against selected job roles.

## Features
- User registration and login
- PDF resume upload
- Resume text extraction
- Skill detection
- Job-role matching
- Missing-skill suggestions
- Clean dashboard
- SQLite by default (works immediately on Windows)
- Optional PostgreSQL configuration through environment variables
- Django admin support

## Windows setup

### 1. Open PowerShell in this project folder

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

### 2. Install packages

```powershell
pip install -r requirements.txt
```

### 3. Create database tables

```powershell
python manage.py migrate
```

### 4. Create an admin account

```powershell
python manage.py createsuperuser
```

### 5. Start the server

```powershell
python manage.py runserver
```

Open:

http://127.0.0.1:8000/

Admin:

http://127.0.0.1:8000/admin/

## Optional PostgreSQL

The project runs with SQLite by default, so no PostgreSQL installation is required.

To use PostgreSQL, set these Windows environment variables before running Django:

```powershell
$env:DB_ENGINE="postgresql"
$env:DB_NAME="resume_analyzer"
$env:DB_USER="postgres"
$env:DB_PASSWORD="your_password"
$env:DB_HOST="localhost"
$env:DB_PORT="5432"
```

Then run:

```powershell
python manage.py migrate
python manage.py runserver
```

## GitHub upload

```powershell
git init
git add .
git commit -m "Initial AI Resume Analyzer project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/AI-Resume-Analyzer.git
git push -u origin main
```

Do not upload your `venv`, database, uploaded private resumes, or secret environment variables.

## Tech stack

- Python
- Django
- SQLite / PostgreSQL
- HTML
- CSS
- PyMuPDF
