from django.contrib.auth.models import User
from django.db import models

class ResumeAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="resumes/")
    job_role = models.CharField(max_length=100)
    detected_skills = models.JSONField(default=list)
    missing_skills = models.JSONField(default=list)
    match_score = models.PositiveIntegerField(default=0)
    extracted_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.job_role} - {self.match_score}%"
