from django import forms

class SymptomForm(forms.Form):
    symptoms = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Describe your symptoms'}),
        label='Symptoms'
    )