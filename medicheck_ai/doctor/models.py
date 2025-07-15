from django.db import models

from django.conf import settings

SPECIALIZATION_CHOICES = [

    ('Cardiologist', 'Cardiologist'),

    ('Dermatologist', 'Dermatologist'),

    ('Neurologist', 'Neurologist'),

    ('General Physician', 'General Physician'),
    
]

class Doctor(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    specialization = models.CharField(max_length=100, choices=SPECIALIZATION_CHOICES)

    bio = models.TextField(blank=True)

    availability = models.CharField(max_length=255, help_text="e.g., Mon-Fri 10am-5pm")

    profile_picture = models.ImageField(upload_to='doctor_profiles/', blank=True, null=True)

    class Meta:

        verbose_name = "Doctor"

        verbose_name_plural = "Doctors"

        ordering = ['specialization']  

    def __str__(self):
        
        return f"Dr. {self.user.get_full_name()} - {self.specialization}"
