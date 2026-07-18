import joblib
import pandas as pd
import os
import sys

# Allow access to src folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.url_features import analyze_url, explain_risk

# Load the trained model
model = joblib.load("models/kitsune_model.pkl")


def predict_url(url):
    # Extract features
    features = analyze_url(url)
    reasons = explain_risk(url)

    # Convert to DataFrame
    X = pd.DataFrame([features])

    # Convert True/False to 1/0
    X = X.astype(int, copy=False)

    # Predict
    prediction = model.predict(X)[0]

    # Confidence
    confidence = model.predict_proba(X).max() * 100

    return prediction, confidence, features, reasons