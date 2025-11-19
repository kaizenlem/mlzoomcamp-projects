from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model and feature columns from disk
model = joblib.load('clv_model.joblib')
feature_columns = joblib.load('feature_columns.joblib')

app = FastAPI()

# Define input data schema using Pydantic
class CLVFeatures(BaseModel):
    first_purchase: int
    last_purchase: int
    product_diversity: int
    recency: int

@app.post("/predict")
def predict_clv(data: CLVFeatures):
    # Arrange incoming features in correct order
    input_data = [getattr(data, col) for col in feature_columns]
    input_arr = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_arr)[0]
    return {"predicted_clv": float(prediction)}
