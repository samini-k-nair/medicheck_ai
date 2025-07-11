
from django.urls import path
from .views import RiskAssessmentView

urlpatterns = [
    path('risk-test/', RiskAssessmentView.as_view(), name='risk-assessment'),  # ✅ Named URL
]
