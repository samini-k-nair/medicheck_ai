# train_model.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib


symptoms = [
    "cough fever sore throat",
    "fever cough sore throat",            # variation
    "runny nose sneezing",
    "sneezing runny nose allergy",
    "headache fever body ache",
    "body ache fever headache",           # variation
    "fever and body ache",
    "chest pain shortness of breath",
    "shortness of breath chest tightness",
    "rash itching skin",
    "itching and rash",
    "stomach pain diarrhea",
    "diarrhea and abdominal cramps",
    "chest pressure sweating nausea",
    "dry flaky skin itching",
    "persistent worry restlessness sleep problem",
]

labels = [
    "Common Cold",
    "Common Cold",
    "Allergy",
    "Allergy",
    "Flu",
    "Flu",
    "Flu",
    "COVID-19",
    "COVID-19",
    "Skin Allergy",
    "Skin Allergy",
    "Food Poisoning",
    "Food Poisoning",
    "Acute Coronary Syndrome",
    "Eczema",
    "Generalized Anxiety Disorder",
]


# 2. Convert text to numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(symptoms)

# 3. Train Naive Bayes model
model = MultinomialNB()
model.fit(X, labels)

# 4. Save model and vectorizer
joblib.dump(model, 'symptom_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("✅ Model and vectorizer saved!")