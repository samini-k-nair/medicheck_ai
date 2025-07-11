from django.db import models
from django.conf import settings

class RiskAssessment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    age = models.IntegerField()
    bmi = models.FloatField()
    smoking = models.BooleanField()
    alcohol_consumption = models.BooleanField()
    physical_activity = models.CharField(max_length=50, choices=[
        ('low', 'Low'), ('moderate', 'Moderate'), ('high', 'High')
    ])
    family_history = models.BooleanField()

    score = models.IntegerField()
    category = models.CharField(max_length=50)  # Low, Moderate, High risk

    assessed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"RiskAssessment for {self.user.username} ({self.category})"
