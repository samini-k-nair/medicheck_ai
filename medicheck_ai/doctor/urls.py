from django.urls import path

from .views import DoctorDashboardView, DoctorProfileView,AppointmentDetailView


app_name = 'doctor'

urlpatterns = [
    path('dashboard/', DoctorDashboardView.as_view(), name='doctor-dashboard'),

    path('profile/', DoctorProfileView.as_view(), name='doctor-profile'),

    path('appointment/<int:pk>/', AppointmentDetailView.as_view(), name='doctor-appointment-detail'),
]
