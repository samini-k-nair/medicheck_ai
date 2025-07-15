from django.db import models

from authentication.models import User  # Your custom user model

class PatientProfile(models.Model):

    user = models.OneToOneField( User,on_delete=models.CASCADE,limit_choices_to={'role': 'Patient'}
    )
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ])
    contact = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - Patient"

    class Meta:
        verbose_name = "Patient Profile"
        verbose_name_plural = "Patient Profiles"
        ordering = ['user__username']
