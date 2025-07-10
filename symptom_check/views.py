

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SymptomForm
from .ai_model import predict_disease
from .models import SymptomCheck

@login_required
def symptom_checker_view(request):
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            symptoms = form.cleaned_data['symptoms']
            predictions = predict_disease(symptoms)
            print("PREDICTIONS:", predictions)  # Debug

            # Handle empty or invalid prediction
            if not predictions or not isinstance(predictions, list):
                return render(request, 'symptom_check/prediction_result.html', {
                    'symptoms': symptoms,
                    'error_message': "Sorry, we couldn't identify a disease based on the entered symptoms."
                })

            first_prediction = predictions[0]

            # If the prediction doesn't contain 'disease' key
            if 'disease' not in first_prediction:
                return render(request, 'symptom_check/prediction_result.html', {
                    'symptoms': symptoms,
                    'error_message': "Sorry, we couldn't identify a disease based on the entered symptoms."
                })

            predicted_disease = first_prediction['disease']

            # Doctor mapping
            disease_specialist_map = {
                'Common Cold': 'General Physician',
                'Flu': 'General Physician',
                'Heart Disease': 'Cardiologist',
                'Diabetes': 'Endocrinologist',
                'Hypertension': 'Cardiologist',
                'Asthma': 'Pulmonologist',
                'Skin Infection': 'Dermatologist',
                'Depression': 'Psychiatrist',
                'Tuberculosis': 'Pulmonologist',
                'Alopecia': 'Dermatologist',
                'Hair Fall': 'Dermatologist',
            }

            doctor = disease_specialist_map.get(predicted_disease, 'General Physician')

            results = [{
                'disease': predicted_disease,
                'doctor': doctor
            }]

            # Save to database
            SymptomCheck.objects.create(
                user=request.user,
                symptoms=symptoms,
                predicted_diseases=predicted_disease
            )

            return render(request, 'symptom_check/prediction_result.html', {
                'symptoms': symptoms,
                'results': results
            })

    else:
        form = SymptomForm()

    return render(request, 'symptom_check/symptom_form.html', {'form': form})
