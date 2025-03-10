import streamlit as st

# Title of the app
st.title("Unit Converter")
st.write("Convert different units easily!")

# Dropdown to select the conversion type
conversion_type = st.selectbox("Choose Conversion Type:", ["Length", "Weight", "Temperature"])

# Input box for value
value = st.number_input("Enter value to convert:", min_value=0.0, format="%.2f")

# Conversion Logic
if conversion_type == "Length":
    st.subheader("Length Converter")
    unit = st.radio("Select Unit:", ["Meters to Feet", "Feet to Meters"])
    if unit == "Meters to Feet":
        result = value * 3.28084
        st.success(f"{value} meters = {result:.2f} feet")
    else:
        result = value / 3.28084
        st.success(f"{value} feet = {result:.2f} meters")

elif conversion_type == "Weight":
    st.subheader("Weight Converter")
    unit = st.radio("Select Unit:", ["Kg to Pounds", "Pounds to Kg"])
    if unit == "Kg to Pounds":
        result = value * 2.20462
        st.success(f"{value} kg = {result:.2f} lbs")
    else:
        result = value / 2.20462
        st.success(f"{value} lbs = {result:.2f} kg")

elif conversion_type == "Temperature":
    st.subheader("Temperature Converter")
    unit = st.radio("Select Unit:", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
    if unit == "Celsius to Fahrenheit":
        result = (value * 9/5) + 32
        st.success(f"{value}°C = {result:.2f}°F")
    else:
        result = (value - 32) * 5/9
        st.success(f"{value}°F = {result:.2f}°C")
