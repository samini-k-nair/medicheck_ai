# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from authentication.models import User  # import your custom User model
# from .models import PatientProfile     # import PatientProfile from current app

# @receiver(post_save, sender=User)
# def create_patient_profile(sender, instance, created, **kwargs):
#     if created and instance.role == 'Patient':
#         PatientProfile.objects.create(user=instance)
