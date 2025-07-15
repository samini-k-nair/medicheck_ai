from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView
from django.urls import reverse
from .forms import RiskAssessmentForm
from .models import RiskAssessment
from .utils import calculate_risk_score

class RiskAssessmentView(View):
    def get(self, request):
        form = RiskAssessmentForm()
        return render(request, 'risk_assessment/form.html', {'form': form})

    def post(self, request):
        form = RiskAssessmentForm(request.POST)
        if form.is_valid():
            # 1. Calculate risk
            data = form.cleaned_data
            score, category = calculate_risk_score(data)

            # 2. Save the assessment
            risk = form.save(commit=False)
            risk.user = request.user
            risk.score = score
            risk.category = category
            risk.save()

            # 3. Redirect to detail page for this risk assessment
            return redirect('risk_assessment:detail', pk=risk.pk)

        # If form invalid, re-render form with errors
        return render(request, 'risk_assessment/form.html', {'form': form})

class RiskAssessmentDetailView(DetailView):
    model = RiskAssessment
    template_name = 'risk_assessment/detail.html'
    context_object_name = 'risk'
