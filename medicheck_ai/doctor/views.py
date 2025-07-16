from django.shortcuts import render, get_object_or_404, render

from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Doctor

from appointments.models import Appointment

from django.views.generic.detail import DetailView

from reports.models import Report

from risk_assessment.models import RiskAssessment

from prescriptions.models import Prescription

from django.views.generic import TemplateView

class DoctorDashboardView(LoginRequiredMixin, View):

    template_name = 'doctor/dashboard.html'


    def get(self, request):

        doctor = get_object_or_404(Doctor, user=request.user)

        appointments = Appointment.objects.filter(doctor=doctor).order_by('preferred_date')

          # Fetch prescriptions for this doctor
        prescriptions = Prescription.objects.filter(doctor=request.user).order_by('-created_at')

        


        return render(request,'doctor/dashboard.html', {

            'doctor': doctor,

            'appointments': appointments,

            'prescriptions' : prescriptions,
        })


class DoctorProfileView(LoginRequiredMixin, View):

    def get(self, request):

        doctor = get_object_or_404(Doctor, user=request.user)

        return render(request, 'doctor/profile.html', {'doctor': doctor})
    
# appointments/views.py

class AppointmentDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        appointment = get_object_or_404(
            Appointment,
            id=pk,
            doctor__user=request.user
        )

        # These lines should be indented with exactly 8 spaces from the `def` line
        reports = Report.objects.filter(user=appointment.user)
        risk_assessment = (
            RiskAssessment.objects
            .filter(user=appointment.user)
            .order_by('-assessed_at')
            .first()
        )

        print("DEBUG reports:", list(reports))
        print("DEBUG risk:", risk_assessment)

        return render(request, 'doctor/appointment_detail.html', {
            'appointment': appointment,
            'reports': reports,
            'risk_assessment': risk_assessment,
        })