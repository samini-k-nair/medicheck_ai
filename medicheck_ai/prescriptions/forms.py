from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class PrescriptionForm(forms.Form):
    patient = forms.ModelChoiceField(queryset=User.objects.filter(is_active=True))
    subject = forms.CharField(initial="Prescription Note")
    body = forms.CharField(widget=forms.Textarea, label="Prescription Text")
