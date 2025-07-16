# reports/urls.py

from django.urls import path
from .views import (
    ReportUploadView,
    ReportListView,
    ReportDownloadView,
    ReportDeleteView 
)

app_name = 'reports'

urlpatterns = [
 
    path('upload/', ReportUploadView.as_view(), name='reports_upload'),
    path('', ReportListView.as_view(), name='report_list'),
    path('<int:pk>/download/', ReportDownloadView.as_view(), name='report_download'),
    path('<int:pk>/delete/', ReportDeleteView.as_view(), name='report_delete'),

    # path('risk-test/', RiskAssessmentView.as_view(), name='risk-assessment'),
]