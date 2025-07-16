import os
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import FileResponse, Http404
from django.urls import reverse_lazy
from .models import Report
from .forms import ReportForm
from appointments.models import Appointment

from django.db.models import Q

# — Upload Page —
class ReportUploadView(LoginRequiredMixin, CreateView):

    model = Report

    form_class = ReportForm

    template_name = 'reports/reports_upload.html'

    success_url = reverse_lazy('reports:report_list')

    def form_valid(self, form):

        form.instance.user = self.request.user

        return super().form_valid(form)
# — List Page —
class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    template_name = 'reports/report_list.html'
    context_object_name = 'reports'

    def get_queryset(self):
        # Filter reports by the logged-in user
        return Report.objects.filter(user=self.request.user).order_by('-uploaded_at')


# — Download/View Report Endpoint —
class ReportDownloadView(LoginRequiredMixin, DetailView):
    model = Report

    def get(self, request, *args, **kwargs):
        report = self.get_object()
        user = request.user

        is_patient = (report.user == user)
        is_doctor = (
            report.appointment is not None and
            report.appointment.doctor.user == user
        )
        if not (is_patient or is_doctor):
            raise Http404("You don't have permission…")

        return FileResponse(
            report.file.open('rb'),
            as_attachment=True,
            filename=report.file.name
        )

# — Delete Report Confirmation & Handling —
class ReportDeleteView(LoginRequiredMixin, DeleteView):
    model = Report
    template_name = 'reports/report_confirm_delete.html'
    success_url = reverse_lazy('report_list')

    def get_queryset(self):
      Report.objects.filter(user=self.request.user)