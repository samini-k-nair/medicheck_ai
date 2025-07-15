from django.shortcuts import render, get_object_or_404,redirect

from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Doctor

from appointments.models import Appointment

from django.views.generic.detail import DetailView

from reports.models import Report

from risk_assessment.models import RiskAssessment

class DoctorDashboardView(LoginRequiredMixin, View):

    def get(self, request):

        doctor = get_object_or_404(Doctor, user=request.user)

        appointments = Appointment.objects.filter(doctor=doctor).order_by('preferred_date')


        return render(request,'doctor/dashboard.html', {

            'doctor': doctor,

            'appointments': appointments,
        })


class DoctorProfileView(LoginRequiredMixin, View):

    def get(self, request):

        doctor = get_object_or_404(Doctor, user=request.user)

        return render(request, 'doctor/profile.html', {'doctor': doctor})
    
class AppointmentDetailView(LoginRequiredMixin, View):

    def get(self, request, pk):

        appointment = get_object_or_404(Appointment, id=pk, doctor__user=request.user)
        
        reports = appointment.reports.all()

        risk_assessment = (RiskAssessment.objects
                           .filter(user=appointment.user)
                           .order_by('-created_at')
                           .first()# most recent
        )

        return render(request, 'doctor/appointment_detail.html', {

            'appointment': appointment,

            'reports': reports,
            
            'risk_assessment': risk_assessment
        })