# Diabetes Prediction Web App

This is a web application that predicts the likelihood of a diabetes attack based on user-provided input. It utilizes a machine learning model trained on various health parameters and demographic information. Users can enter their gender, age, hypertension status, heart disease history, smoking history, BMI (Body Mass Index), HbA1c level, and blood glucose level to obtain a prediction.

![Diabetes Prediction](https://images.squarespace-cdn.com/content/v1/5beb1276365f0260572d41cd/1542866801904-NGKEOBM6CT6950DIU53Q/Diabetes.jpg)

## Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

### Features

- Predicts the likelihood of a diabetes attack based on user inputs.
- Accepts user inputs for gender, age, hypertension, heart disease, smoking history, BMI, HbA1c level, and blood glucose level.
- Provides a descriptive sentence along with the prediction result.

### Technologies Used

- Python
- Flask (for the web application)
- Scikit-learn (for machine learning)
- HTML/CSS (for the user interface)

## Getting Started

To run the web application locally, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/diabetes-prediction-app.git

2. Navigate to the project directory:

```bash
cd diabetes-prediction-app

3. Install the required dependencies:

```bash
pip install -r requirements.txt

4. Run the Flask application:

```bash
python app.py

5. Open your web browser and go to http://localhost:5000 to access the web application.


## Usage

1. Fill out the form on the web page with the following information:

   - Gender
   - Age
   - Hypertension status (Yes or No)
   - Heart disease history (Yes or No)
   - Smoking history
   - BMI (Body Mass Index)
   - HbA1c level
   - Blood glucose level

2. Click the "Predict" button.

3. The application will display a prediction result along with a descriptive sentence indicating the likelihood of a diabetes attack.




