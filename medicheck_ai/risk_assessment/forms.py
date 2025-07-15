from django import forms
from .models import RiskAssessment

class RiskAssessmentForm(forms.ModelForm):
    class Meta:
        model = RiskAssessment
        
        exclude = ['user', 'score', 'category', 'assessed_at']

        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control'}),

            'bmi': forms.NumberInput(attrs={'class': 'form-control'}),

            'smoking': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'alcohol_consumption': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'physical_activity': forms.Select(attrs={'class': 'form-control'}),

            'family_history': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
