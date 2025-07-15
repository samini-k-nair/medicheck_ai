# appointments/views.py

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView, DetailView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Appointment
from .forms import AppointmentForm
from doctor.models import Doctor
from reports.models import Report
from risk_assessment.models import RiskAssessment

class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/appointment_form.html'

    def form_valid(self, form):
        print("✅ form_valid called")
        print("Submitted data:", form.cleaned_data)

        self.object = form.save(commit=False)
        self.object.user = self.request.user

        specialization = form.cleaned_data.get('doctor_type')
        print(f"Looking up doctor for specialization: {specialization}")

        doctor = Doctor.objects.filter(specialization=specialization).first()
        print(f"Found doctor: {doctor}")

        if not doctor:
            form.add_error('doctor_type', 'No doctor available for that specialization')
            return self.form_invalid(form)

        self.object.doctor = doctor
        self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print("❌ form_invalid called!")
        print("Form errors:", form.errors.as_json())
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('appointments:appointment_success', kwargs={'pk': self.object.pk})


class AppointmentSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'appointments/appointment_success.html'


class AppointmentDetailView(LoginRequiredMixin, DetailView):
    model = Appointment
    template_name = 'appointments/appointment_detail.html'
    context_object_name = 'appointment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        appointment = self.object

        # Reports uploaded by the patient
        context['reports'] = appointment.reports.all()

        # Latest risk assessment using the correct timestamp field
        context['risk_assessment'] = (
            RiskAssessment.objects
            .filter(user=appointment.user)
            .order_by('-assessed_at')
            .first()
        )
        return context
