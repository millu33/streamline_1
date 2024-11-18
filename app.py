import streamlit as st
import numpy as np
import pickle
import sklearn as sk

st.write("Hello Everyone!")

st.header("Obesity Predictor")

st.write("Enter your data below:")
st.write("Please provide weight in Kilograms to 1 dp such as 64.0, and height in Meters to 2 dp such as 1.87.")
st.write("For your gender, put 1 for the relevant category and leave the other field 0.")

age = st.number_input("Age")
weight = st.number_input("Weight")
height = st.number_input("Height")
gender_male = st.number_input("Gender_Male")
gender_female = st.number_input("Gender_Female")

obesity_predicted = np.array([(age, weight, height, gender_male, gender_female)])

with open('rf.pkl', 'rb') as f:
    model = pickle.load(f)

prediction = model.predict(obesity_predicted)
st.write(prediction)

st.write("Interpretation of Results:")
st.write("0 = Insufficient Weight")
st.write("1 = Normal Weight")
st.write("2 = Obesity Type I")
st.write("3 = Obesity Type II")
st.write("4 = Obesity Type III")
st.write("5 = Overweight Level I")
st.write("6 = Overweight Level II")