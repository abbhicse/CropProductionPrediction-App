import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("models/model_rf.joblib")
le_area = joblib.load("models/le_area.joblib")
le_item = joblib.load("models/le_item.joblib")

st.title("Crop Production Predictor")

area = st.selectbox("Select Area", le_area.classes_)
item = st.selectbox("Select Crop", le_item.classes_)
year = st.slider("Select Year", 1961, 2022)
area_harvested = st.number_input("Area Harvested (ha)")
yield_val = st.number_input("Yield (kg/ha)")

if st.button("Predict"):
    area_encoded = le_area.transform([area])[0]
    item_encoded = le_item.transform([item])[0]

    features = [[area_encoded, item_encoded, year, area_harvested, yield_val]]
    prediction = model.predict(features)
    
    st.success(f"Estimated Production: {prediction[0]:,.2f} tons")
