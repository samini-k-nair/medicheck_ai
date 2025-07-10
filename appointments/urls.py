from django.urls import path
from .views import AppointmentCreateView, AppointmentSuccessView

urlpatterns = [
    path('', AppointmentCreateView.as_view(), name='appointment_page'),
    path('success/', AppointmentSuccessView.as_view(), name='appointment_success'),
]
