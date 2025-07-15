
from django.db import models

from django.conf import settings

from doctor.models import Doctor  # Import the Doctor model


DOCTOR_SPECIALTIES = [

    ('General Physician', 'General Physician'),

    ('Cardiologist', 'Cardiologist'),

    ('Dermatologist', 'Dermatologist'),

    ('Psychiatrist', 'Psychiatrist'),

    ('Pulmonologist', 'Pulmonologist'),
    # Add more as needed
]

class Appointment(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)

    age = models.PositiveIntegerField()

    gender = models.CharField(max_length=10)

    symptoms = models.TextField()

    doctor_type = models.CharField(max_length=50, choices=DOCTOR_SPECIALTIES)

    preferred_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments', null=True, blank=True)

    prescription = models.TextField(blank=True, null=True)

    def __str__(self):

        return f"{self.full_name} - {self.doctor_type} ({self.preferred_date})"

    class Meta:

        verbose_name = "Appointment"

        verbose_name_plural = "Appointments"

        ordering = ['-created_at']
        
        # db_table = 'appointments_appointment'
