
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model and preprocessor
model = joblib.load("autoworth_model_deployment_compressed.pkl")
preprocessor = joblib.load("autoworth_preprocessor.pkl")

# App title
st.title("🚗 AutoWorth AI")
st.write("Used Car Price & Deal Advisor")

st.subheader("Enter Car Information")

# User inputs
make = st.selectbox(
    "Make",
    ["Audi", "BMW", "Ford", "Hyundai", "Mercedes",
     "Skoda", "Toyota", "Vauxhall", "Volkswagen"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic", "Semi-Auto", "Other"]
)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "Hybrid", "Electric", "Other"]
)

year = st.number_input(
    "Year",
    min_value=1990,
    max_value=2024,
    value=2020,
    step=1
)

mileage = st.number_input(
    "Mileage",
    min_value=0.0,
    value=30000.0,
    step=1000.0
)

mpg = st.number_input(
    "MPG",
    min_value=0.0,
    value=40.0,
    step=1.0
)

enginesize = st.number_input(
    "Engine Size",
    min_value=0.0,
    value=1.5,
    step=0.1
)

tax = st.number_input(
    "Tax",
    min_value=0.0,
    value=150.0,
    step=10.0
)

seller_price = st.number_input(
    "Seller Price",
    min_value=0.0,
    value=15000.0,
    step=500.0
)

# Predict price
if st.button("Predict Price"):

    # Calculate engineered features
    reference_year = 2024

    car_age = reference_year - year

    if car_age <= 0:
        car_age = 1

    mileage_per_year = mileage / car_age
    engine_size_per_age = enginesize / car_age

    # Create input dataframe
    car_data = pd.DataFrame({
        "transmission": [transmission],
        "mileage": [mileage],
        "fuel_type": [fuel_type],
        "mpg": [mpg],
        "enginesize": [enginesize],
        "make": [make],
        "tax": [tax],
        "car_age": [car_age],
        "mileage_per_year": [mileage_per_year],
        "engine_size_per_age": [engine_size_per_age]
    })

    # Preprocess and predict
    processed_car = preprocessor.transform(car_data)
    predicted_price = model.predict(processed_car)[0]

    # Deal Advisor
    difference = predicted_price - seller_price
    percentage_difference = (difference / predicted_price) * 100

    if percentage_difference > 10:
        rating = "🟢 Great Deal"
    elif percentage_difference >= 5:
        rating = "🟢 Good Deal"
    elif percentage_difference >= -5:
        rating = "🟡 Fair Price"
    elif percentage_difference >= -10:
        rating = "🟠 Slightly Overpriced"
    else:
        rating = "🔴 Overpriced"

    # Display results
    st.subheader("💰 Estimated Market Price")
    st.write(f"£{predicted_price:,.2f}")

    st.subheader("🏷️ Seller Price")
    st.write(f"£{seller_price:,.2f}")

    if difference >= 0:
        st.write(f"Difference: £{difference:,.2f} cheaper")
    else:
        st.write(f"Difference: £{abs(difference):,.2f} more expensive")

    st.write(f"Price Difference: {percentage_difference:.2f}%")

    st.subheader("📊 Deal Rating")
    st.write(rating)
