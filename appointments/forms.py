from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['full_name', 'age', 'gender', 'symptoms', 'doctor_type', 'preferred_date']

        widgets = {
            'full_name': forms.TextInput(attrs={
                                                'class': 'form-control',
                                                'required': 'required',
                                                'placeholder': 'Enter your full name' }),

            'age': forms.NumberInput(attrs={
                
                                            'class': 'form-control', 
                                            'required': 'required', 
                                            'min': 0, 'placeholder': 'Age' }),


            'gender': forms.Select(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
                                   attrs={'class': 'form-control', 
                                          'required': 'required'}),

            'symptoms': forms.Textarea(attrs={
                                              'class': 'form-control',
                                              'rows': 3, 
                                              'placeholder': 'Describe your symptoms' }),
            'doctor_type': forms.Select(attrs={
                                              'class': 'form-control',
                                               'required': 'required'  }),
          'preferred_date': forms.DateInput(attrs={
                                                 'class': 'form-control',
                                                 'type': 'date'})  # ✅ This makes it show a calendar picker
        }
