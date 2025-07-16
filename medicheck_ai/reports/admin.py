# reports/admin.py

from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'user',
        'uploaded_at',
        'has_file',
    ]
    list_filter = ['uploaded_at', 'user']
    search_fields = ['title', 'user__username']
    readonly_fields = ['uploaded_at', 'has_file']
