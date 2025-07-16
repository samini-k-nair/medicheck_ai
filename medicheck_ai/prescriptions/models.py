from django.db import models
from django.conf import settings
from appointments.models import Appointment

class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='prescriptions', null=True,
     blank=True,)
    STATUS_CHOICES = [('draft','Draft'), ('sent','Sent')]

    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='prescribed', on_delete=models.CASCADE)
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='prescriptions', on_delete=models.CASCADE)
    subject = models.CharField(max_length=200, default='Prescription Note')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return f"Rx #{self.id} to {self.patient.get_full_name()} on {self.created_at:%Y-%m-%d}"
