# from django.shortcuts import render,redirect

# from django.views import View

# from django.contrib.auth import authenticate, login, logout

# from .forms import LoginForm

# # ----------------------------
# # Login View
# # ----------------------------
# class LoginView(View):

#     def get(self, request, *args, **kwargs):

#         form = LoginForm()

#         data = {'page': 'login-page','form':form}

#         return render(request, 'authentication/login.html',context=data)

#     def post(self, request, *args, **kwargs):

#         form = LoginForm(request.POST) 

#         error =  None

#         if form.is_valid():  # form valid or not

#             username = form.cleaned_data.get('username')

#             password = form.cleaned_data.get('password')

#             user = authenticate(username=username,password=password)

#             if user :

#                 login(request,user)

#                 return redirect('symptom_checker')
            
#             error = 'invalid credentials'
            
#         data = {'form': form, 'error':error}

#         return render(request, 'authentication/login.html',context=data)


          

# # # ----------------------------
# # # Logout View
# # # ----------------------------
# # class LogoutView(View):

# #     def get(self, request, *args, **kwargs):

# #         logout(request)

# #         return redirect('home')  # redirect to login page after logout

# # # ----------------------------
# # # Register Choices View
# # # ----------------------------
# # class RegisterChoicesView(View):

# #     def get(self, request, *args, **kwargs):

# #         return render(request,'authentication/register_choices.html')

# #     def post(self, request, *args, **kwargs):

# #         role = request.POST.get('role')

# #         if role == 'patient':

# #             return redirect('patient-register')
        
# #         elif role == 'doctor':

# #             return redirect('doctor-details')
        



from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from authentication.models import User

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


# ----------------------------
# Register View
# ----------------------------
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
            login(request, user)
            return redirect('symptom_checker')
        return render(request, 'authentication/register.html', {'form': form})
