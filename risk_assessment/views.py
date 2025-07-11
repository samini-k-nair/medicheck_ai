# from django.shortcuts import render

# # Create your views here.
# from django.views.generic import TemplateView

# class RiskTestView(TemplateView):
#     template_name = 'risk_assessment/risk_test.html'



from django.shortcuts import render, redirect
from django.views import View
from .forms import RiskAssessmentForm
from .utils import calculate_risk_score
from .models import RiskAssessment

class RiskAssessmentView(View):
    def get(self, request):
        form = RiskAssessmentForm()
        return render(request, 'risk_assessment/form.html', {'form': form})

    def post(self, request):
        form = RiskAssessmentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            score, category = calculate_risk_score(data)

            # Save
            risk = form.save(commit=False)
            risk.user = request.user
            risk.score = score
            risk.category = category
            risk.save()

            return render(request, 'risk_assessment/result.html', {
                'risk': risk
            })

        return render(request, 'risk_assessment/form.html', {'form': form})
