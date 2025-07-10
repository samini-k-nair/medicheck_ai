# from django import forms

# class LoginForm(forms.Form):

#     username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={
#                                                                            'class':'form-control',
#                                                                            'required':'required',
#                                                                            }))
#     password =forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={
#                                                                            'class':'form-control',
#                                                                            'required':'required',
#                                                                            }))

# authentication/forms.py

from django import forms
from authentication.models import User  # Ensure your custom user model is imported

# ✅ Login Form
class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'required': 'required',
        })
    )
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'required': 'required',
        })
    )

# ✅ Register Form
class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': 'required'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': 'required'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password']  # role should exist in your User model
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'required'}),
            'role': forms.Select(attrs={'class': 'form-control', 'required': 'required'}),
        }
        help_texts = {
            'username': '',  
        }    

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
