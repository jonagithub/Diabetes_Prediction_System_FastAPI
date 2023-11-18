import json
import requests

# url for the API endpoint
url = 'http://127.0.0.1:8000/diabetes_prediction'

# Input data for the model
input_data_for_model = {
    'Pregnancies': 5,
    'Glucose': 166,
    'BloodPressure': 72,
    'SkinThickness': 19,
    'Insulin': 175,
    'BMI': 25.8,
    'DiabetesPedigreeFunction': 0.587,
    'Age': 51
}

# Convert input data to JSON format
input_json = json.dumps(input_data_for_model)

# Make a POST request to the API endpoint
response = requests.post(url, data=input_json)

# Print the response from the API
print(response.text)