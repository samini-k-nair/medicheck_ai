
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from authentication.models import User
from patient.models import PatientProfile  

# ----------------------------
# Login View
# ----------------------------
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'authentication/login.html', {'form': form, 'page': 'login-page'})

    def post(self, request):
        form = LoginForm(request.POST)
        error = None
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('symptom_checker')
            error = 'Invalid credentials'
        return render(request, 'authentication/login.html', {'form': form, 'error': error})
    
    #  logout view
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')    


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'authentication/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # ✅ Create PatientProfile if role is Patient
            if user.role == 'Patient':
                PatientProfile.objects.create(
                    user=user,
                    age=form.cleaned_data.get('age'),
                    gender=form.cleaned_data.get('gender'),
                    contact=form.cleaned_data.get('contact'),
                    address=form.cleaned_data.get('address'),
                )

            login(request, user)
            return redirect('symptom_checker')

        return render(request, 'authentication/register.html', {'form': form})
