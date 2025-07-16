from django.views.generic import FormView
from django.core.mail import EmailMultiAlternatives
from django.urls import reverse_lazy
from django.conf import settings
from .models import Prescription
from .forms import PrescriptionForm

class PrescriptionCreateView(FormView):
    template_name = 'prescriptions/new.html'
    form_class = PrescriptionForm
    success_url = reverse_lazy('prescriptions:new')

    def form_valid(self, form):
        rx = Prescription.objects.create(
            doctor=self.request.user,
            patient=form.cleaned_data['patient'],
            subject=form.cleaned_data['subject'],
            body=form.cleaned_data['body'],
            status='sent',
        )
        # Send email
        msg = EmailMultiAlternatives(
            subject=rx.subject,
            body=rx.body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[rx.patient.email],
        )
        msg.send(fail_silently=False)
        return super().form_valid(form)
