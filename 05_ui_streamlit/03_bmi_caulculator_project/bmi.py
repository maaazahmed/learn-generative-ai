import streamlit as st


st.title("Welcome to BMI Calculator")


weight = st.number_input("Enter your weight (in kgs)")


status = st.selectbox("Select your height format:",  ('cms', 'meters', 'feet'))

if status == "cms":
    height = st.number_input("Centimeters")
    try:
        bmi =  weight / ((height/100)**2)
    except:
        st.text("Enter some value of height")    