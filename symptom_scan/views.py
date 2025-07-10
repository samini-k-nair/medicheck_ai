from django.shortcuts import render



from django.views import View

# Create your views here.
class HomeView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'symptom_scan/home.html')
    
class LoginView(View):

    def get(self,request,*args,**kwargs):

      return render(request,'authentication/login.html')    
    
class Symptom_checkerView(View):

    def get(self,request,*args,**kwargs):

      return render(request,'symptom_scan/symptom_checker.html')    
