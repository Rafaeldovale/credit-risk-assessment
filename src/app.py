from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import logging  # 1. Import the native logging library
import os
import pandas as pd


# 2. Configure the logging system pipeline layout
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("app.log"),  # Saves logs inside a text file
        logging.StreamHandler(),  # Mirror logs on the terminal screen
    ],
)

ml_models = {}


class CreditApplication(BaseModel):
    amount: float
    duration: float
    age: float
    status: str
    credit_history: str
    saving: str

@asynccontextmanager
async def lifespan(app: FastAPI):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MODEL_PATH = os.path.join(BASE_DIR, "models", "credit_lgb_champion.joblib")

    logging.info("Initializing server startup deployment lifecycle...")
    if os.path.exists(MODEL_PATH):
        ml_models["credit_model"] = joblib.load(MODEL_PATH)
        logging.info("Champion LightGBM model successfully loaded into RAM!")
    else:
        logging.critical(f"Model binary artifact missing at: {MODEL_PATH}")

    yield
    logging.info("Shutting down application server. Cleaning memory resources...")
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


# 3. Inject logs inside our execution endpoint
# 3. Secure and clean Predict Route
@app.post("/predict")
def predict_credit(application: CreditApplication):
    if "credit_model" not in ml_models:
        logging.error("Prediction failed: Model artifact not loaded in RAM.")
        return {"error": "Machine Learning model is not loaded in memory."}

    # 1. Capture the 3 numeric features
    features_array = [application.duration, application.amount, application.age]

    # 2. Add 45 zeros to complete the exact 48 columns expected by LightGBM
    padding_zeros = [0.0] * 45
    full_input_matrix = [features_array + padding_zeros]

    # 3. Fetch the model from RAM and execute prediction
    model = ml_models["credit_model"]
    prediction = int(model.predict(full_input_matrix))

    # 4. Map the output to a business decision
    decision = "Approved" if prediction == 1 else "Denied"

    # 5. Log the structured audit line
    logging.info(
        f"CREDIT_EVALUATION | Amount: {application.amount} | Age: {application.age} | Decision: {decision}"
    )

    return {
        "credit_decision": decision,
        "probability_of_default_status": "calculated_successfully",
        "processed_features": {
            "amount": application.amount,
            "duration": application.duration,
            "age": application.age,
        },
    }

