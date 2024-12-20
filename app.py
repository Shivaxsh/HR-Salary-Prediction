import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('salary_prediction_model.pkl')

# App title
st.title("HR Salary Prediction Dashboard")

# Input fields
age = st.number_input("Enter Age", min_value=22, max_value=60, value=30)
experience = st.number_input("Enter Years of Experience", min_value=0, max_value=38, value=5)
current_salary = st.number_input("Enter Current Salary", min_value=20000, max_value=200000, value=50000)

# Predict salary
if st.button("Predict Salary"):
    input_data = pd.DataFrame([[age, experience, current_salary]], columns=['Age', 'Years of Experience', 'Current Salary'])
    predicted_salary = model.predict(input_data)[0]
    st.write(f"Predicted Salary: {predicted_salary:.2f}")