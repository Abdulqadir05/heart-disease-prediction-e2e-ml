import streamlit as st
import pandas as pd
import joblib

# -----------------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------------
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

# -----------------------------------------------------------
# ULTRA DARK-NEON CSS
# -----------------------------------------------------------
st.markdown("""
<style>

body {
    background: #000000;
}

.main-title {
    font-size: 46px;
    font-weight: 900;
    text-align: center;
    color: #ff0066;
    text-shadow: 0px 0px 25px #ff0066;
    padding-bottom: 20px;
}

.card {
    background: rgba(15, 15, 15, 0.55);
    border: 1px solid rgba(255, 255, 255, 0.12);
    padding: 25px;
    border-radius: 18px;
    backdrop-filter: blur(12px);
    box-shadow: 0 0 30px rgba(255,0,102,0.2);
}

label, .stMarkdown, .css-16huue1, .css-17eq0hr, .css-1fv8s86 {
    color: white !important;
}

.stSelectbox div, .stNumberInput div, .stSlider > div > div > div {
    color: white !important;
}

.stSlider > div > div > div {
    background: #ff0066 !important;
}

.prob-box {
    background: rgba(255,0,90,0.25);
    border: 1px solid #ff0066;
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    font-size: 22px;
    color: white;
    margin-bottom: 10px;
    text-shadow: 0px 0px 12px #ff0066;
}

.risk-low {
    background: #009432;
    padding: 10px 20px;
    border-radius: 12px;
    color: white;
    font-size: 20px;
    display: inline-block;
}

.risk-medium {
    background: #fbc531;
    padding: 10px 20px;
    border-radius: 12px;
    color: black;
    font-size: 20px;
    display: inline-block;
}

.risk-high {
    background: #EA2027;
    padding: 10px 20px;
    border-radius: 12px;
    color: white;
    font-size: 20px;
    display: inline-block;
}

.footer {
    text-align: center;
    margin-top: 40px;
    font-size: 14px;
    color: #aaaaaa;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------
# LOAD MODEL
# -----------------------------------------------------------
model = joblib.load("heart_disease_model.pkl")

# -----------------------------------------------------------
# HEADER
# -----------------------------------------------------------
st.markdown("<div class='main-title'>💓  HEART DISEASE PREDICTION SYSTEM</div>", unsafe_allow_html=True)
st.write("### Dark-Neon Medical AI • Powered by your Gradient Boosting Model")
st.markdown("---")

# -----------------------------------------------------------
# LAYOUT
# -----------------------------------------------------------
left, right = st.columns([1.5, 1])

with left:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🧍 Patient Information")

    age = st.number_input("Age", 20, 100, 45)
    sex = st.selectbox("Sex", ["M", "F"])
    cp = st.selectbox("Chest Pain Type", ["ATA", "NAP", "ASY", "TA"])
    resting_bp = st.number_input("Resting BP (mmHg)", 50, 250, 120)
    chol = st.number_input("Cholesterol (mg/dL)", 0, 600, 200)
    fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
    restecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
    maxhr = st.number_input("Max Heart Rate Achieved", 60, 220, 150)
    exercise = st.selectbox("Exercise Angina", ["Y", "N"])
    oldpeak = st.slider("Oldpeak", -2.0, 6.0, 1.0, 0.1)
    st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------------
# PREDICTION
# -----------------------------------------------------------
with right:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🚨 Risk Prediction")

    data = pd.DataFrame({
        "Age": [age],
        "Sex": [sex],
        "ChestPainType": [cp],
        "RestingBP": [resting_bp],
        "Cholesterol": [chol],
        "FastingBS": [fasting_bs],
        "RestingECG": [restecg],
        "MaxHR": [maxhr],
        "ExerciseAngina": [exercise],
        "Oldpeak": [oldpeak],
        "ST_Slope": [st_slope],
    })

    if st.button("🔍 Predict", use_container_width=True):
        pred = model.predict(data)[0]
        prob = model.predict_proba(data)[0][1] * 100

        st.markdown(f"<div class='prob-box'>Probability: <b>{prob:.2f}%</b></div>", unsafe_allow_html=True)

        if prob < 40:
            st.markdown("<div class='risk-low'>LOW RISK</div>", unsafe_allow_html=True)
        elif prob < 70:
            st.markdown("<div class='risk-medium'>MEDIUM RISK</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='risk-high'>HIGH RISK</div>", unsafe_allow_html=True)

        st.progress(int(prob))

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<p class='footer'>⚠️ Not a medical device. For educational use only.</p>", unsafe_allow_html=True)
