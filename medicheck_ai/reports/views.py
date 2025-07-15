import os
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView
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
        # If the appointment's PK is passed via URL as 'appointment_pk'
        appointment = get_object_or_404(
            Appointment,
            pk=self.kwargs.get('appointment_pk'),
            user=self.request.user
        )
        form.instance.appointment = appointment
        return super().form_valid(form)

# — List Page —
class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    template_name = 'reports/report_list.html'
    context_object_name = 'reports'

    def get_queryset(self):
        return Report.objects.filter(appointment__user=self.request.user).order_by('-uploaded_at')

# — Download/View Report Endpoint —
class ReportDownloadView(LoginRequiredMixin, View):
    def get(self, request, pk):
        report = get_object_or_404(
            Report,
            Q(appointment__user=request.user) |
            Q(appointment__doctor__user=request.user),
            pk=pk
        )
        if not (report.file.name and report.file.storage.exists(report.file.name)):
            raise Http404("Sorry, this file doesn't exist.")
        file_handle = report.file.open('rb')
        filename = os.path.basename(report.file.name)
        return FileResponse(
            file_handle,
            as_attachment=True,
            filename=filename
        )

# — Delete Report Confirmation & Handling —
class ReportDeleteView(LoginRequiredMixin, DeleteView):
    model = Report
    template_name = 'reports/report_confirm_delete.html'
    success_url = reverse_lazy('report_list')

    def get_queryset(self):
        return Report.objects.filter(appointment__user=self.request.user)
