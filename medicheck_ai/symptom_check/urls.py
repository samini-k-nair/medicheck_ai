from django.urls import path
from .views import symptom_checker_view  # ✅ make sure this is correct

urlpatterns = [

     path('', symptom_checker_view, name='symptom_checker'),
    #  path('<int:appointment_id>/', symptom_checker_view, name='symptom_checker'),


   

]
