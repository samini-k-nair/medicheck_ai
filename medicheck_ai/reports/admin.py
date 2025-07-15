from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'appointment', 'uploaded_at')
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('appointment')
