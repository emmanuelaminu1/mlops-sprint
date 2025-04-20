# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from app.model import model

app = FastAPI()

class InputData(BaseModel):
    data: list  # List of 4 floats for Iris

@app.get("/")
def root():
    return {"message": "ML API is alive"}

@app.post("/predict")
def predict(input_data: InputData):
    preds = model.predict([input_data.data])
    return {"prediction": int(preds[0])}
