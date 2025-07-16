from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title','file']
        def clean_title(self):
           title = self.cleaned_data.get('title', '').strip()
           if not title:
              raise forms.ValidationError("Please enter a report title.")
           return title
