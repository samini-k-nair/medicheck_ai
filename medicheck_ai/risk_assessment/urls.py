from django.urls import path
from .views import RiskAssessmentView, RiskAssessmentDetailView

app_name = 'risk_assessment'

urlpatterns = [
    path('risk-test/', RiskAssessmentView.as_view(), name='risk-assessment'),
    path('<int:pk>/detail/', RiskAssessmentDetailView.as_view(), name='detail'),
    # Missing create? Add it:
    path('create/<int:appointment_pk>/', RiskAssessmentView.as_view(), name='create'),
]
