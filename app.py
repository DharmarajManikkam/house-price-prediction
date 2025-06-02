# app.py
from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

# Load the model
with open("models/house_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "Welcome to the House Price Prediction API!"}

@app.post("/predict")
def predict(total_rooms: float):
    input_data = pd.DataFrame([[total_rooms]], columns=["total_rooms"])
    prediction = model.predict(input_data)[0]
    return {"predicted_price": prediction}
