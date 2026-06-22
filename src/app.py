from fastapi import FastAPI
import joblib
import os

# 1. Initialize the FastApi application instance
app = FastAPI(
    title="Credit Risk Assessment API",
    description="Production API to predict the Probability of Default (PD) using LightGBM.",
    version="1.0.0",
)

# 2. Define the absolute path to load our serialized champion model
MODEL_PATH = os.getenv("MODEL_PATH", "models/credit_lgb_champion.joblib")

# 3. Create the base check endpoint (Health Check)
@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Credit Risk Assessment API is running successfully.",
    }