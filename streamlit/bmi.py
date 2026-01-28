import streamlit as st
st.title("BMI Calculator")
st.subheader("Enter your details:")

weight = st.number_input("Weight (in kilograms)")
height = st.number_input("Height (in meters)")
if st.button("Calculate BMI"):
        bmi = weight / (height ** 2)
        st.success(f"HI user your bmi result is {bmi}")