import os
import joblib

# Load model and vectorizer
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'symptom_model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'vectorizer.pkl')

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# Get all known vocabulary terms from training
known_words = set(vectorizer.vocabulary_.keys())

def predict_disease(symptoms_input):
    symptoms_input = symptoms_input.lower().strip()
    input_words = symptoms_input.split()

    # ✅ Check how many input words are known
    matched = [word for word in input_words if word in known_words]
    match_ratio = len(matched) / len(input_words) if input_words else 0

    # ❌ Reject if less than 50% words match
    if match_ratio < 0.5:
        return []  # Triggers error message in the view

    # ✅ Predict if input is valid
    X_test = vectorizer.transform([symptoms_input])
    prediction = model.predict(X_test)
    probas = model.predict_proba(X_test)
    confidence = max(probas[0])

    return [{
        "disease": prediction[0],
        "confidence": round(float(confidence), 2)
    }]
