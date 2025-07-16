from django.urls import path
from .views import PrescriptionCreateView

app_name = 'prescriptions'
urlpatterns = [
    path('new/', PrescriptionCreateView.as_view(), name='new'),
]
