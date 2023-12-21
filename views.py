from django.shortcuts import render
from sklearn.preprocessing import LabelEncoder
import joblib
import os


def predict_d(request):
    if request.method == 'POST':
        gender = request.POST['gender']
        label_encoder = LabelEncoder()
        gender_encoded =  label_encoder.fit_transform([gender])[0]
        age = float(request.POST['age'])
        hypertension = float(request.POST['hypertension'])
        heart_disease = float(request.POST['heart_disease'])
        smoking_history = request.POST['smoking_history']
        label_encoder = LabelEncoder()
        smoking_encoded =  label_encoder.fit_transform([smoking_history])[0]
        bmi = float(request.POST['bmi'])
        HbA1c_level = float(request.POST['HbA1c_level'])
        blood_glucose_level = float(request.POST['blood_glucose_level'])
        file_path = os.path.join(os.path.dirname(__file__), 'diabetes_model.pkl')
        model = joblib.load(file_path)
        predicted_d = model.predict([[gender_encoded, age, hypertension, heart_disease, smoking_encoded, bmi, HbA1c_level, blood_glucose_level]])
      
        context = {'predicted_d': predicted_d[0]}
        return render(request, 'result.html', context)
        
    return render(request, 'index.html')

def eda_view(request):
    return render(request, 'eda.html')




