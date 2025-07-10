from django.urls import path
from .views import RiskTestView

urlpatterns = [
    path('', RiskTestView.as_view(), name='risk_test_page'),
]
