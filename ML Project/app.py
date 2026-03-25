import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model_5_features.pkl")

# Title
st.title("🎮 Gaming Addiction Predictor")

st.write("Enter user details:")

# Inputs (True / False using radio buttons)
withdrawal = st.radio("Withdrawal Symptoms", ["Yes", "No"])
loss_interest = st.radio("Loss of Other Interests", ["Yes", "No"])
continued = st.radio("Continued Despite Problems", ["Yes", "No"])

isolation = st.slider("Social Isolation Score", 0, 10)
face_to_face = st.number_input("Face-to-Face Social Hours Weekly", 0.0, 20.0)

# Predict button
if st.button("Predict"):

    # Convert Yes/No → 1/0
    input_data = pd.DataFrame([{
        'withdrawal_symptoms': 1 if withdrawal == "Yes" else 0,
        'loss_of_other_interests': 1 if loss_interest == "Yes" else 0,
        'continued_despite_problems': 1 if continued == "Yes" else 0,
        'social_isolation_score': isolation,
        'face_to_face_social_hours_weekly': face_to_face
    }])

   
    prediction = model.predict(input_data)[0]

    if prediction == 3:
        st.error("⚠️ Severe Risk of Gaming Addiction")
    elif prediction==2:
        st.error("⚠️ High Risk of Gaming Addiction")
    elif prediction==1:
        st.success("✅ Moderate Risk of Gaming Addiction")
    else:
        st.success("✅ Low Risk of Gaming Addiction")