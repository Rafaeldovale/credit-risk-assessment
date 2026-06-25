# 🏦 Credit Risk Assessment Project

<!-- Tech Stack Badges -->
![Python](https://shields.io)
![FastAPI](https://shields.io)
![Docker](https://shields.io)
![Scikit-Learn](https://shields.io)

## 📌 Project Overview
This repository contains an enterprise-grade, End-to-End Classic Machine Learning solution designed to evaluate bank customer creditworthiness and predict the Probability of Default (PD). This project bridges the gap between interactive data science exploration and mature, containerized MLOps architecture.

```text
credit-risk-assessment/
│
├── data/
│   ├── raw/                  <-- Source 'GermanCredit.csv' dataset
│   └── processed/            <-- Sanitized target frames
│
├── models/                   <-- Serialized production binaries (.joblib)
│   └── credit_lgb_champion.joblib
│
├── src/                      <-- Core microservice source code
│   ├── app.py                <-- FastAPI routing & predictive execution
│   └── app.log               <-- Automated production auditing log file
│
├── notebook/                 <-- Interactive prototyping notebooks
│   └── exploration.ipynb
│
├── Dockerfile                <-- Multi-layer Docker orchestration receipt
├── requirements.txt          <-- Fixed python dependencies environment
└── README.md                 <-- Comprehensive system documentation
```

## 📊 Business Problem & Metrics
In credit scoring, misclassifying a defaulting customer as a good payer (**False Negative**) is significantly more expensive than misclassifying a good payer as a defaulter (**False Positive**) due to severe capital degradation. 

Our modeling strategy prioritizes optimizing:
- 🎯 **Recall / Sensitivity**: To capture as many defaulters as possible.
- 📈 **Precision**: To optimize the credit approval rate and maximize corporate interest revenue.
- 📉 **Auditing Capabilities**: Providing full tracking through compliance logs.

---

## 🔬 Model Tournament & Performance Benchmarking

During the exploration phase, we built an interactive benchmarking tournament across multiple algorithms on 200 unseen testing samples:

| Machine Learning Model | Overall Accuracy | Precision (Good Payer) | Recall (Good Payer) | Default Catch Rate (Bad Payer) |
| :--- | :---: | :---: | :---: | :---: |
| **Logistic Regression** | 67.50% | 83.78% | 66.43% | **70.00%** |
| **Random Forest** | 72.00% | 75.61% | 88.57% | 33.33% |
| **LightGBM (Champion)** | **74.00%** | **81.43%** | **81.43%** | 55.00% |
| **XGBoost** | 71.00% | 82.03% | 75.00% | 61.67% |

### 🏆 The Champion Veredict
While **Logistic Regression** was highly conservative (catching 70% of bad payers but rejecting too many good customers), **LightGBM** was selected as the production **Champion**. It achieved the highest overall accuracy (74%) and established a perfect business equilibrium, approving 81.43% of honest borrowers while keeping precision solid at 81.43%, maximizing net bank revenue.

---

## 🛠️ Tech Stack & Environment Setup

Follow these steps to set up the development environment and run the project locally.

### 1. Clone the Repository
```bash
git clone https://github.com/Rafaeldovale/credit-risk-assessment
cd credit-risk-assessment
```

### 2. Set Up the Virtual Environment (Local Development venv)
```bash
# On Windows:
python -m venv venv
.\venv\Scripts\activate

# On macOS / Linux:
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Project Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run Locally (Uvicorn Dev Mode)
```bash
cd src
uvicorn app:app --reload
```
👉 Access local documentation at: `http://localhost:8000/docs`

---

## 🐳 MLOps Orchestration (Production Docker Containerization)

To eliminate environmental variance, the entire application is containerized using **Docker** into an isolated Debian-slim Linux environment equipped with native C++ multi-processing dependencies (`libgomp1`).

### 🛠️ Execution Guide (Docker Terminal Commands)

1. **Build the Docker Production Image:**
   ```bash
   docker build -t credit-risk-api:v1 .
   ```

2. **Launch the Containerized Server:**
   ```bash
   docker run -d -p 8000:8000 --name credit_server credit-risk-api:v1
   ```

3. **Interact with the Automated Swagger UI Documentation:**
   👉 `http://localhost:8000/docs`

4. **Audit and Inspect Real-time Server Logs:**
   ```bash
   docker logs credit_server
   ```

---

## 🗃️ Compliance & Auditing Sample Log Output

Every incoming client credit evaluation automatically triggers an immutable auditing log line inside `app.log` for institutional compliance tracking:

```text
2026-06-25 04:12:05 [INFO] Initializing server startup deployment lifecycle...
2026-06-25 04:12:06 [INFO] Champion LightGBM model successfully loaded into RAM!
2026-06-25 06:18:07 [INFO] CREDIT_EVALUATION | Amount: 2000.0 | Age: 45.0 | Decision: Denied
2026-06-25 06:22:14 [INFO] CREDIT_EVALUATION | Amount: 250.0  | Age: 65.0 | Decision: Approved
```

---
Developed by **Rafael Bezerra do Vale** | *AI Engineer & Machine Learning Specialist*
