# reports/models.py

from django.db import models
from django.conf import settings  # recommended for refering to the user model


class Report(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reports'
    )
    # doctor = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, 
    #     on_delete=models.CASCADE, 
    #     null=True, blank=True,
    #     related_name='assigned_reports'
    # )
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='reports/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       
        title_display= self.title or "(Untitled report#{self.id})"
        return f"{title_display} – by {self.user.username}"
    @property
    def has_file(self):
        return bool(self.file.name) and self.file.storage.exists(self.file.name)

    class Meta:
        verbose_name = "Medical Report"
        verbose_name_plural = "Medical Reports"
        ordering = ['-uploaded_at']
        db_table = 'appointment_reports'