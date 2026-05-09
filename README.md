# Wine-Quality
# 🍷 Wine Quality Prediction using Machine Learning

## 📌 Overview

This project explores the use of machine learning models to predict wine quality based on physicochemical attributes such as acidity, alcohol content, and sulphates.

Two approaches were implemented:

* **Regression** to predict exact quality scores (e.g., 3–8)
* **Classification** to categorize wines into *low* vs *high* quality

The project highlights the trade-off between prediction precision and real-world usability.

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
* Target:

  * Regression: Quality score (integer)
  * Classification: Binary label (low vs high quality)

---

## 🔍 Exploratory Data Analysis

* Analyzed feature distributions and correlations
* Identified **alcohol** and **sulphates** as strong predictors of quality
* Observed moderate correlations, suggesting nonlinear relationships

---

## ⚙️ Models Implemented

### Regression Models

* Linear Regression
* Decision Tree Regressor
* Support Vector Regression (SVR)
* Neural Network (MLP Regressor)

### Classification Models

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* Support Vector Machine (SVM)

---

## 📈 Results

### Regression Performance

| Model             | MAE | RMSE |
| ----------------- | --- | ---- |
| Linear Regression | X   | X    |
| Decision Tree     | X   | X    |
| SVR (Best)        | X   | X    |
| Neural Network    | X   | X    |

* **SVR achieved the lowest error**, making it the best regression model
* Performance was limited by **label noise** due to subjective wine ratings

---

### Classification Performance

| Model                | Precision | Recall | F1-score |
| -------------------- | --------- | ------ | -------- |
| Logistic Regression  | X         | X      | X        |
| Decision Tree        | X         | X      | X        |
| Random Forest (Best) | X         | X      | X        |
| SVM                  | X         | X      | X        |

* **Random Forest performed best**, especially in identifying high-quality wines
* Classification achieved stronger metrics due to reduced problem complexity

---

## 🧠 Key Insights

* Wine quality prediction is constrained by **subjective human ratings**, introducing noise into the dataset
* **Nonlinear models** (SVR, Random Forest) outperform linear models
* Chemical attributes alone cannot fully explain perceived wine quality
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

## 🚀 Future Improvements

* Hyperparameter tuning (GridSearchCV)
* Cross-validation for more robust evaluation
* Deployment as a web app (e.g., Streamlit)
* Incorporating additional data sources (e.g., sensory reviews)

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib, Seaborn

---

## 💡 Takeaway

This project demonstrates that machine learning performance is not only dependent on model choice, but also on **data quality and problem formulation**. By reframing the problem from regression to classification, more practical and reliable predictions can be achieved.


https://wine-quality-app-app-nkp9aalz5nfgya5umbhfdi.streamlit.app/
