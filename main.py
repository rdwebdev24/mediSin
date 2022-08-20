import pickle
from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from starlette.responses import JSONResponse
import numpy as np
import pandas as pd

loaded_model = pickle.load(open('model.h5', 'rb'))

DATA_PATH = "./Training.csv"
data = pd.read_csv(DATA_PATH).dropna(axis = 1)
X = data.iloc[:,:-1]
y = data.iloc[:,-1]

symptoms = X.columns.values

symptom_index = {}
for index, value in enumerate(symptoms):
    symptom = " ".join([i.capitalize() for i in value.split("_")])
    symptom_index[symptom] = index

data_dict = {
    "symptom_index":symptom_index,
    "predictions_classes":y
}

def predictDisease(symptoms):
    try:
        symptoms = symptoms.split(",")
        input_data = [0] * len(data_dict["symptom_index"])
        for symptom in symptoms:
            index = data_dict["symptom_index"][symptom]
            input_data[index] = 1
         
        input_data = np.array(input_data).reshape(1,-1)
        svm_prediction = data_dict["predictions_classes"][loaded_model.predict(input_data)[0]] 
    except:
        return "invalid input"
    else:
        return svm_prediction
 

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return JSONResponse(status_code=200,content = {"Server":"Up"}) 

@app.get("/run")
def read_item(q: Union[str, None] = None):
    predict = predictDisease(q)
    body = {'res' : predict}
    return JSONResponse(status_code=200,content = body)
    