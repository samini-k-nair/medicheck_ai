from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import Appointment
from .forms import AppointmentForm

# ✅ Appointment Form View (Class-based)
class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/appointment_form.html'
    success_url = reverse_lazy('appointment_success')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Attach the logged-in user to the appointment
        return super().form_valid(form)

# ✅ Appointment Success View
class AppointmentSuccessView(TemplateView):
    template_name = 'appointments/appointment_success.html'
