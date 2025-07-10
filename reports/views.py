# reports/views.py

import os
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import FileResponse, Http404
from django.urls import reverse_lazy
from .models import Report
from .forms import ReportForm
# — Upload Page —
class ReportUploadView(LoginRequiredMixin, CreateView):
    model = Report
    form_class = ReportForm
    template_name = 'reports/upload_report.html'
    success_url = reverse_lazy('reports_list')  # Redirect to list page after upload

    def form_valid(self, form):
        # Assign the current user to the report before saving
        form.instance.user = self.request.user
        return super().form_valid(form)

# — List Page —
class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    template_name = 'reports/report_list.html'
    context_object_name = 'reports'

    def get_queryset(self):
        # Only show reports belonging to the current user
        return Report.objects.filter(user=self.request.user).order_by('-uploaded_at')

# — Download/View Report Endpoint —
class ReportDownloadView(LoginRequiredMixin, View):
    def get(self, request, pk):
        report = get_object_or_404(Report, pk=pk, user=request.user)
        # Ensure the file exists before serving
        if not (report.file.name and report.file.storage.exists(report.file.name)):
            raise Http404("Sorry, this file doesn't exist.")
        file_handle = report.file.open('rb')
        filename = os.path.basename(report.file.name)
        return FileResponse(
            file_handle,
            as_attachment=True,    # Force download prompt
            filename=filename      # Use just the basename
        )

# — Delete Report Confirmation & Handling —
# At the end of reports/views.py


class ReportDeleteView(LoginRequiredMixin, DeleteView):
    model = Report
    template_name = 'reports/report_confirm_delete.html'
    success_url = reverse_lazy('reports_list')

    def get_queryset(self):
        return Report.objects.filter(user=self.request.user)
