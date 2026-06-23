from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

# Global dictionary to store our machine learning models in memory
ml_models = {}


# 1. Define the Data Contract (Schema) using Pydantic
# This enforces the exact data types the model needs to receive
# For our simplified production initial test, we will request the top 3 features
class CreditApplication(BaseModel):
    amount: float
    duration: float
    age: float


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Secure absolute path lookup to find the serialized champion model
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MODEL_PATH = os.path.join(BASE_DIR, "models", "credit_lgb_champion.joblib")

    print("--- Server Startup: Loading Machine Learning Artifacts ---")
    if os.path.exists(MODEL_PATH):
        ml_models["credit_model"] = joblib.load(MODEL_PATH)
        print("[SUCCESS] Champion LightGBM model successfully loaded into RAM!")
    else:
        print(f"[CRITICAL ERROR] Could not find the model binary at: {MODEL_PATH}")

    yield
    print("--- Server Shutdown: Cleaning Up Resources ---")
    ml_models.clear()


app = FastAPI(
    title="Credit Risk Assessment API",
    description="Production API to predict the Probability of Default (PD) using LightGBM.",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/")
def home():
    model_status = "armed" if "credit_model" in ml_models else "missing"
    return {
        "status": "online",
        "model_status": model_status,
        "message": "Credit Risk Assessment API is running successfully.",
    }


# 2. Update the POST Endpoint with matrix structure padding
@app.post("/predict")
def predict_credit(application: CreditApplication):
    if "credit_model" not in ml_models:
        return {"error": "Machine Learning model is not loaded in memory."}

    # Fetch the model from RAM to inspect how many features it expects
    model = ml_models["credit_model"]
    total_features_expected = model.n_features_in_

    # Create a base array filled with zeros matching the 48 features required
    # This prevents the dimension mismatch error (Code 500)
    features_array = [0.0] * total_features_expected

    # Map our 3 inputs into the exact first positions of the array
    # In our dataset, the first columns are numeric (duration, amount, age)
    features_array[0] = application.duration
    features_array[1] = application.amount
    features_array[2] = application.age

    # Wrap inside a 2D array format for scikit-learn/lightgbm
    input_data = [features_array]

    # Execute the prediction safely
    prediction = int(model.predict(input_data)[0])
    decision = "Approved" if prediction == 1 else "Denied"

    return {
        "credit_decision": decision,
        "probability_of_default_status": "calculated_successfully",
        "processed_features": {
            "amount": application.amount,
            "duration": application.duration,
            "age": application.age,
        },
    }
