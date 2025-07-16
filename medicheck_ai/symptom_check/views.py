from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SymptomForm
from .ai_model import predict_disease
from .models import SymptomCheck
# from appointments.models import Appointment

@login_required
def symptom_checker_view(request):
    # appointment = get_object_or_404(Appointment, user=request.user)  # Ensure appointment exists

    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            symptoms = form.cleaned_data['symptoms']
            predictions = predict_disease(symptoms)
            
            # Handle prediction errors
            if not isinstance(predictions, list) or not predictions:
                return render(request, 'symptom_check/prediction_result.html', {
                    'symptoms': symptoms,
                    # 'appointment': appointment,
                    'error_message': "Sorry, we couldn't identify a disease based on the entered symptoms."
                })

            first = predictions[0]
            if 'disease' not in first:
                return render(request, 'symptom_check/prediction_result.html', {
                    'symptoms': symptoms,
                    # 'appointment': appointment,
                    'error_message': "Sorry, we couldn't identify a disease based on the entered symptoms."
                })

            predicted_disease = first['disease']
            disease_specialist_map = {
                'Common Cold': 'General Physician',
                'Flu': 'General Physician',
                'Heart Disease': 'Cardiologist',
                'Diabetes': 'Endocrinologist',
                'Hypertension': 'Cardiologist',
                'Asthma': 'Pulmonologist',
                'Skin Allergy': 'Dermatologist',
                'Depression': 'Psychiatrist',
                'Tuberculosis': 'Pulmonologist',
                'Alopecia': 'Dermatologist',
                'Hair Fall': 'Dermatologist',
            }
            doctor = disease_specialist_map.get(predicted_disease, 'General Physician')
            results = [{'disease': predicted_disease, 'doctor': doctor}]

            SymptomCheck.objects.create(
                user=request.user,
                symptoms=symptoms,
                predicted_diseases=predicted_disease
            )

            return render(request, 'symptom_check/prediction_result.html', {
                'symptoms': symptoms,
                'results': results,
                # 'appointment': appointment  # make appointment available to template
            })
    else:
        form = SymptomForm()

    return render(request, 'symptom_check/symptom_form.html', {
        'form': form,
        # 'appointment': appointment
    })
