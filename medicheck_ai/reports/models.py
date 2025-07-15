


from django.db import models
from appointments.models import Appointment

class Report(models.Model):
    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.CASCADE,
        related_name='reports',null=True, blank=True)
    
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='reports/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Safely include appointment full_name if it exists
        if self.appointment and getattr(self.appointment, 'full_name', None):
            return f"{self.title} – {self.appointment.full_name}"
        return f"{self.title} – [No appointment]"

    @property
    def has_file(self):
        return bool(self.file.name) and self.file.storage.exists(self.file.name)

    class Meta:
        verbose_name = "Medical Report"
        verbose_name_plural = "Medical Reports"
        ordering = ['-uploaded_at']
        db_table = 'appointment_reports'  # Custom table name
