# from django.contrib import admin

# # Register your models here.
# from . import models

# admin.site.register(models.PatientProfile)







from django.contrib import admin
from .models import PatientProfile

@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'gender', 'contact']
    search_fields = ['user__username', 'user__email']
    list_filter = ['gender']
