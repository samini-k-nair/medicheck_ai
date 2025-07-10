# reports/urls.py

from django.urls import path
from .views import (
    ReportUploadView,
    ReportListView,
    ReportDownloadView,
    ReportDeleteView 
)

urlpatterns = [
    path('upload/',   ReportUploadView.as_view(), name='reports_upload'),
    path('list/',     ReportListView.as_view(),   name='reports_list'),
    path('download/<int:pk>/', ReportDownloadView.as_view(), name='report_download'),
    path('delete/<int:pk>/',   ReportDeleteView.as_view(),   name='report_delete'),
]
