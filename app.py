from flask import Flask, render_template, request
import joblib
import pickle

app = Flask(__name__)

with open('diabetes_prediction_app\model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


@app.route('/')
def index():
    return render_template('index.html')


gender_mapping = {'0': 'Male', '1': 'Female'}
smoking_history_mapping = {
    'never': 0,
    'No Info': 1,
    'current': 2,
    'former': 3,
    'ever': 4,
    'not current': 5
}


@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve input data from the form as before
    gender = request.form.get('gender')
    age = request.form.get('age')
    hypertension = request.form.get('hypertension')
    heart_disease = request.form.get('heart_disease')
    smoking_history = request.form.get('smoking_history')
    bmi = request.form.get('bmi')
    HbA1c_level = request.form.get('HbA1c_level')
    blood_glucose_level = request.form.get('blood_glucose_level')

    # Check if any of the form fields are empty
    if not all([gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level]):
        error_message = "Please fill in all the fields."
        return render_template('index.html', error_message=error_message)

    # Convert input values to the appropriate data types
    gender = int(gender)
    age = float(age)
    hypertension = int(hypertension)
    heart_disease = int(heart_disease)
    smoking_history = smoking_history_mapping[smoking_history]
    bmi = float(bmi)
    HbA1c_level = float(HbA1c_level)
    blood_glucose_level = float(blood_glucose_level)

    # Perform predictions using your loaded model
    result = model.predict([[gender, age, hypertension, heart_disease,
                           smoking_history, bmi, HbA1c_level, blood_glucose_level]])[0]

    # Create a descriptive sentence based on the prediction
    if result == 1:
        smoking_status = "smokes" if smoking_history == 2 else "formerly smoked" if smoking_history == 1 else "never smoked"
        prediction_sentence = f"For a {'female' if gender == 1 else 'male'} of {int(age)} years with a blood glucose level of {blood_glucose_level}, a BMI of {bmi}, and a smoking history of {smoking_status}, the chance of a diabetes attack is high."
    else:
        smoking_status = "smokes" if smoking_history == 2 else "formerly smoked" if smoking_history == 1 else "never smoked"
        prediction_sentence = f"For a {'female' if gender == 1 else 'male'} of {int(age)} years with a blood glucose level of {blood_glucose_level}, a BMI of {bmi}, and a smoking history of {smoking_status}, the chance of a diabetes attack is low."

    print("Prediction Sentence:", prediction_sentence)
    return render_template('index.html', prediction_sentence=prediction_sentence)


if __name__ == '__main__':
    app.run(debug=True)
