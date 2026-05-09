# 🍷 Wine Quality Prediction using Machine Learning

## 🚀 Live Demo

👉 https://wine-quality-app-app-nkp9aalz5nfgya5umbhfdi.streamlit.app/

---

## Overview

This project builds an end-to-end machine learning pipeline to predict wine quality based on physicochemical attributes such as acidity, alcohol content, and sulphates.

It combines:

* **Data analysis & modeling (Jupyter Notebook)**
* **Interactive deployment (Streamlit web app)**

Two approaches were explored:

* **Regression** to predict exact quality scores (e.g., 3–8)
* **Classification** to categorize wines into *low* vs *high* quality

The project highlights the trade-off between prediction precision and real-world usability.

---

## Web Application

An interactive Streamlit app was developed to make the model usable in real time.

Users can:

* Input chemical properties of wine
* Receive **predicted quality score (SVR)**
* Receive **quality classification (Random Forest)**

This transforms the project from a static analysis into a **user-facing ML application**.

---

## 🎯 Objectives

* Predict wine quality using chemical features
* Compare performance across multiple machine learning models
* Evaluate differences between regression and classification approaches
* Analyze limitations caused by subjective human ratings

---

## 📊 Dataset

* Source: UCI Wine Quality Dataset
* Features: 11 chemical attributes (e.g., alcohol, pH, citric acid)

**Target:**

* Regression: Quality score (integer)
* Classification: Binary label (low vs high quality)

---

## Exploratory Data Analysis

* Analyzed feature distributions and correlations
* Identified **alcohol** and **sulphates** as strong predictors of quality
* Observed moderate correlations, suggesting nonlinear relationships

---

## Models Implemented

### Regression Models

* Multiple Linear Regression
* Simple Linear Regression
* Decision Tree Regressor
* Support Vector Regression (SVR)
* Neural Network (MLP Regressor)

### Classification Models

* Logistic Regression
* Random Forest Classifier
* Support Vector Classifier (SVC)

---

## 📈 Results

### Regression Performance

| Model                      | MAE        | RMSE        |
| -------------------------- | -----------| ----------- |
| SVR (Best)                 | 0.460600   | 0.622400    |
| Multiple Linear Regression | 0.486761   | 0.633244    |
| MLP                        | 0.496621   | 0.637176    |
| Simple Linear Regression   | 0.523097   | 0.662312    |
| Regression Tree            | 0.524100   | 0.664700    |

* **SVR achieved the lowest error**, making it the best regression model
* Performance was limited by **label noise** due to subjective wine ratings

---

### Classification Performance

| Model                | Precision | Recall | F1-score |
| -------------------- | --------- | ------ | -------- |
| Random Forest (Best) | 0.84      | 0.81   | 0.8214   |
| SVC                  | 0.82      | 0.74   | 0.7762   |
| Logistic Regression  | 0.80      | 0.75   | 0.7711   |


* **Random Forest performed best**, especially in identifying high-quality wines
* Classification achieved stronger metrics due to reduced problem complexity

---

## 🧠 Key Insights

* Wine quality prediction is constrained by **subjective human ratings**, introducing noise into the dataset
* **Nonlinear models** (SVR, Random Forest) outperform linear models
* Chemical attributes alone do not fully explain perceived wine quality
* Simplifying the problem (classification) improves model performance

---

## ⚖️ Regression vs Classification

| Approach       | Strengths               | Limitations        |
| -------------- | ----------------------- | ------------------ |
| Regression     | Precise predictions     | Sensitive to noise |
| Classification | More robust, actionable | Loss of detail     |

* Regression is better for **detailed analysis**
* Classification is better for **practical decision-making**

---

## Future Improvements

* Hyperparameter tuning (GridSearchCV)
* Cross-validation for more robust evaluation

---

## Tools used

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib, Seaborn
* **Streamlit (for deployment)**

---

## 💡 Takeaway

This project demonstrates that machine learning performance is not only dependent on model choice, but also on **data quality and problem formulation**.

By extending the analysis into a deployed web application, the project showcases how machine learning models can be translated into **practical, user-facing tools**.

