# 💓 Heart Disease Prediction — End-to-End Machine Learning Pipeline

An advanced clinical risk prediction system using **EDA**, **statistical tests**, **preprocessing pipelines**, **Gradient Boosting**, **Optuna tuning**, and a deployed **Streamlit App** with modern UI.


---

## 🚀 Project Overview

This project builds a complete **End-to-End Heart Disease Prediction System** using a structured ML workflow:


- ✔ Exploratory Data Analysis (EDA)

- ✔ Data cleaning & imputation

- ✔ Statistical tests (Chi-square, t-test)

- ✔ Encoding & scaling using `ColumnTransformer`

- ✔ Gradient Boosting Classifier with **Optuna tuning**

- ✔ Evaluation (AUC, Recall, Precision)

- ✔ Saving deployable ML pipeline

- ✔ Dark-neon **Streamlit Web App** for real-time prediction


This is a **production-grade ML project** suitable for deployment and portfolio use.


---

## 📊 Dataset Summary

The dataset contains **918 patient records** with features such as:


- Age  
- Sex  
- Chest Pain Type  
- Resting BP  
- Cholesterol  
- Fasting Blood Sugar  
- Resting ECG  
- Max Heart Rate  
- Exercise Angina  
- Oldpeak  
- ST Slope  


Target variable: **HeartDisease (0 or 1)**


---

## 🔍 Key EDA Insights

- 172 entries had **Cholesterol = 0** → fixed using median imputation  
- 1 entry had **RestingBP = 0**  
- 79% samples are **Male**, 21% **Female**  
- ASY chest pain strongly indicates disease  
- Oldpeak & MaxHR are highly influential  
- Useful correlations found among clinical features  


Full EDA in: `reports/Heart_failure.pdf`


---

## 🧠 Modeling Approach

### 🔧 Preprocessing

- OneHotEncoding for categoricals  
- RobustScaler for numeric data  
- All transformations inside a single **Pipeline**  
- Prevents leakage and is deployment-safe  


### 🔥 Final Model

- **GradientBoostingClassifier**
- Tuned using Optuna  
- Final Metrics:  
  - **AUC:** ~0.94  
  - **Recall:** ~0.91  


---

## 🎯 Optuna Hyperparameter Tuning

Optimized parameters include:

- n_estimators  
- learning_rate  
- max_depth  
- subsample  
- min_samples_split  
- min_samples_leaf  


---

## 🤖 Saved Model

📦 `model/heart_disease_model.pkl`  
Contains the full pipeline:

- Preprocessor  
- Encoder  
- Scaler  
- Final Gradient Boosting Model  

---

## 🛠️ Tech Stack

**Languages & Libraries**
- 🐍 **Python 3.10**
- 📘 **Pandas**
- 📊 **NumPy**
- 🤖 **Scikit-Learn**
- 🔧 **Joblib**

**Modeling & Optimization**
- 🌲 Gradient Boosting Classifier  
- 🎯 Optuna (Hyperparameter Tuning)  
- ⚙️ ColumnTransformer Pipeline  

**Visualization**
- 📈 Matplotlib  
- 📊 Seaborn  

**Deployment**
- 🌐 Streamlit (Dark-Neon UI)  
- 📦 Deployed Model: `.pkl` Pipeline  

**Tools**
- 📝 Jupyter Notebook  
- 🐙 GitHub (Version Control)  
- 🧪 Statistical Testing: Chi-square, T-test  

---
---

## 👤 Author

**Abdul Qadir**  
🎓 **Program:** B.S. in Applied AI & Data Science  
🏫 **Institute:** Indian Institute of Technology Jodhpur  
📅 **Date:** December 2025  
📍 India  

🔗 **Connect with me:**  
- GitHub: https://github.com/Abdulaqadir05  
- LinkedIn: https://www.linkedin.com/in/abdul-qadir-533827318/edit/forms/project/new/
-----

### 🌐 Live Streamlit App

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://heart-disease-prediction-e2e-ml-nnwxc55mgbbti5kygvg4f5.streamlit.app/)

