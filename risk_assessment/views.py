from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class RiskTestView(TemplateView):
    template_name = 'risk_assessment/risk_test.html'
