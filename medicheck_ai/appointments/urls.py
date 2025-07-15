# appointments/urls.py
from django.urls import path
from .views import AppointmentCreateView, AppointmentSuccessView,AppointmentDetailView
app_name = 'appointments'

urlpatterns = [
    path('', AppointmentCreateView.as_view(), name='appointment_create'),
    path('success/<int:pk>/', AppointmentSuccessView.as_view(), name='appointment_success'),
    path('<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
]
