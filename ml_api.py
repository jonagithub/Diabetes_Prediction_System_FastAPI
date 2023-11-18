from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

# Defining a Pydantic model named model_input to represent the expected structure of the input data.
class model_input(BaseModel):
    # These are the columns used in diabetes.ipynb
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int       
        
# loading the saved/pre-trained model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# defining API endpoint for prediction
@app.post('/diabetes_prediction')
def diabetes_predd(input_parameters : model_input):
    # extracting the input data from the request as a JSON string and converting it into a Python dictionary 
    # input_data from diabetes.ipynb file
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    preg = input_dictionary['Pregnancies']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']
    
    # creating a list feature and using the loaded model to make a prediction
    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]
    
    prediction = diabetes_model.predict([input_list])
    
    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
    