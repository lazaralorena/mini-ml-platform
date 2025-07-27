"""REST API for serving a trained Machine Learning model using the Iris dataset."""

import os
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# Load the trained model from the serve directory
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)

# Initialize the FastAPI application
app = FastAPI(title="ML Model API")


# Define request body
class Input(BaseModel):
    """Input schema with a list of features (floats)."""

    features: list[float]


# Define prediction endpoint
@app.post("/predict")
def predict(data: Input):
    """Returns the prediction for the provided feature vector."""
    try:
        prediction = model.predict([data.features])
        return {"prediction": int(prediction[0])}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
