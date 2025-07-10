from django.conf import settings   # ✅ Use this!
from django.db import models

class SymptomCheck(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    symptoms = models.TextField()
    predicted_diseases = models.TextField()
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SymptomCheck for {self.user.username} on {self.checked_at.strftime('%Y-%m-%d %H:%M')}"