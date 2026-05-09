
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_absolute_error, mean_squared_error, classification_report

st.set_page_config(page_title="Wine Quality Predictor", page_icon="🍷", layout="centered")

FEATURES = [
    "fixed acidity",
    "volatile acidity",
    "citric acid",
    "residual sugar",
    "chlorides",
    "free sulfur dioxide",
    "total sulfur dioxide",
    "density",
    "pH",
    "sulphates",
    "alcohol",
]

@st.cache_data
def load_data():
    return pd.read_csv("winequality-red.csv")

@st.cache_resource
def train_models():
    df = load_data()

    X = df[FEATURES]
    y_reg = df["quality"]

    # Same train/test split style as the notebook
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_reg, test_size=0.30, random_state=0
    )

    # Best regression model from notebook: SVR with C=1 and scaled features
    svr_model = Pipeline([
        ("scaler", StandardScaler()),
        ("model", SVR(C=1))
    ])
    svr_model.fit(X_train, y_train)
    reg_predictions = svr_model.predict(X_test)
    reg_mae = mean_absolute_error(y_test, reg_predictions)
    reg_rmse = mean_squared_error(y_test, reg_predictions) ** 0.5

    # Classification target: low vs high quality
    # Adjust threshold if your notebook used a different cutoff.
    y_class = (df["quality"] >= 6).astype(int)
    X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(
        X, y_class, test_size=0.30, random_state=0
    )

    # Best classifier from notebook: Random Forest, n_estimators=100, max_depth=15
    rf_model = RandomForestClassifier(
        n_estimators=100,
        max_depth=15,
        random_state=1
    )
    rf_model.fit(X_train_c, y_train_c)
    class_predictions = rf_model.predict(X_test_c)
    report = classification_report(y_test_c, class_predictions, output_dict=True)
    f1_high = report["1"]["f1-score"]
    recall_high = report["1"]["recall"]

    return svr_model, rf_model, reg_mae, reg_rmse, f1_high, recall_high

st.title("🍷 Wine Quality Predictor")
st.write(
    "This app predicts red wine quality using chemical attributes. "
    "It provides both an exact score prediction using SVR and a high/low quality prediction using Random Forest."
)

try:
    df = load_data()
    svr_model, rf_model, reg_mae, reg_rmse, f1_high, recall_high = train_models()
except FileNotFoundError:
    st.error("Missing file: winequality-red.csv. Add the dataset CSV to the same folder as app.py.")
    st.stop()

st.subheader("Enter Wine Chemical Properties")

col1, col2 = st.columns(2)

with col1:
    fixed_acidity = st.number_input("Fixed acidity", value=7.4, min_value=0.0)
    volatile_acidity = st.number_input("Volatile acidity", value=0.70, min_value=0.0)
    citric_acid = st.number_input("Citric acid", value=0.00, min_value=0.0)
    residual_sugar = st.number_input("Residual sugar", value=1.9, min_value=0.0)
    chlorides = st.number_input("Chlorides", value=0.076, min_value=0.0, format="%.3f")
    free_sulfur_dioxide = st.number_input("Free sulfur dioxide", value=11.0, min_value=0.0)

with col2:
    total_sulfur_dioxide = st.number_input("Total sulfur dioxide", value=34.0, min_value=0.0)
    density = st.number_input("Density", value=0.9978, min_value=0.0, format="%.4f")
    ph = st.number_input("pH", value=3.51, min_value=0.0)
    sulphates = st.number_input("Sulphates", value=0.56, min_value=0.0)
    alcohol = st.number_input("Alcohol", value=9.4, min_value=0.0)

input_data = pd.DataFrame([[ 
    fixed_acidity,
    volatile_acidity,
    citric_acid,
    residual_sugar,
    chlorides,
    free_sulfur_dioxide,
    total_sulfur_dioxide,
    density,
    ph,
    sulphates,
    alcohol,
]], columns=FEATURES)

if st.button("Predict Wine Quality"):
    predicted_score = svr_model.predict(input_data)[0]
    predicted_class = rf_model.predict(input_data)[0]
    predicted_probability = rf_model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Results")
    st.metric("Predicted Quality Score", f"{predicted_score:.2f}")

    if predicted_class == 1:
        st.success(f"Classification: High-quality wine ({predicted_probability:.1%} probability)")
    else:
        st.warning(f"Classification: Low-quality wine ({predicted_probability:.1%} probability of high quality)")

    st.caption("High quality is defined as quality score >= 6. Change this threshold in app.py if your notebook uses a different cutoff.")

st.divider()
st.subheader("Model Summary")
st.write("**Regression model:** Support Vector Regression (SVR)")
st.write(f"MAE: {reg_mae:.4f} | RMSE: {reg_rmse:.4f}")
st.write("**Classification model:** Random Forest Classifier")
st.write(f"High-quality wine recall: {recall_high:.4f} | High-quality wine F1-score: {f1_high:.4f}")

st.subheader("About the Project")
st.write(
    "The regression model predicts an exact wine quality score, while the classification model "
    "simplifies the task into low-quality vs high-quality wine. This shows the trade-off between "
    "precision and practical decision-making."
)
