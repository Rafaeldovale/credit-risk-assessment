# 🏦 Credit Risk Assessment Project

<!-- Tech Stack Badges -->
![Python](https://shields.io)
![FastAPI](https://shields.io)
![Docker](https://shields.io)
![Scikit-Learn](https://shields.io)

## 📌 Project Overview
This repository contains an End-to-End Classic Machine Learning solution designed to predict the Probability of Default (PD) for credit applicants. The objective is to minimize financial losses by identifying high-risk customers before credit approval.

```text
credit-risk-assessment/
│
├── data/
│   ├── raw/                  <-- Store 'GermanCredit.csv' here
│   └── processed/            <-- Cleaned data will be saved here
│
├── models/                   <-- Store serialized model binaries (.joblib)
│   └── credit_lgb_champion.joblib
│
├── src/                      <-- Source code (EN-US)
│   ├── __init__.py
│   ├── data_pipeline.py      <-- Data cleaning & processing
│   ├── train.py              <-- Model training script
│   └── app.py                <-- FastAPI application
│
├── notebook/                 <-- Interactive Jupyter Notebooks
│   └── exploration.ipynb
│
├── Dockerfile                <-- Docker configuration
├── requirements.txt          <-- Python dependencies
└── README.md                 <-- Project documentation
```

## 📊 Business Problem & Metrics
In credit scoring, misclassifying a defaulting customer as a good payer (**False Negative**) is significantly more expensive than misclassifying a good payer as a defaulter (**False Positive**). 

Therefore, our modeling strategy prioritizes optimizing:
- 🎯 **Recall / Sensitivity**: To capture as many defaulters as possible.
- 📈 **ROC-AUC**: To evaluate the model's capability to distinguish between classes.
- 📉 **KS (Kolmogorov-Smirnov)**: To measure the maximum separation between good and bad risk distributions.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Machine Learning:** Scikit-Learn
- **API Framework:** FastAPI
- **Containerization:** Docker

## 📐 Project Architecture
Refer to the folder structure outlined in the repository root to navigate through data pipelines, model training, and API deployment steps.

## 🚀 How to Run

Follow these steps to set up the development environment and run the project locally.

### 1. Clone the Repository
```bash
git clone https://github.com/Rafaeldovale/credit-risk-assessment
cd credit-risk-assessment
```

### 2. Set Up the Virtual Environment (venv)
Create and activate an isolated Python environment to manage dependencies:

**On Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Project Dependencies
Upgrade pip and install all required libraries using the requirements file:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the Jupyter Notebook
Open VS Code, navigate to `notebook/exploration.ipynb`, select the project `venv` kernel, and start coding!

---
Developed by **Rafael Bezerra do Vale** | *Data Scientist & Machine Learning Specialist*
