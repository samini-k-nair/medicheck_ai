
import os
from django.db import models
from django.conf import settings

class Report(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='reports/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):    # this
        return f"{self.title} - {self.user.username}"
    
    @property
    def has_file(self):
        return bool(self.file.name) and self.file.storage.exists(self.file.name)
    
    class Meta:
        verbose_name = "Medical Report"
        verbose_name_plural = "Medical Reports"
        ordering = ['-uploaded_at']  # Show newest uploads first
        db_table = 'user_reports'    # Optional: custom database table name

