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
from patient.models import PatientProfile  # ✅ import profile model


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

    # ✅ Additional fields for PatientProfile
    age = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
                               required=False,
                               widget=forms.Select(attrs={'class': 'form-control'}))
    contact = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
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