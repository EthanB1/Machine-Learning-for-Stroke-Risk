#import libararies and dependencies
import streamlit as st

import numpy as np
import pandas as pd
import joblib

#import ML model
#model= joblib.load('')

#Create App Headline
st.title("Are You At Risk of Having Stroke? :health_worker:")
#Create health information input options
gender = st.selectbox("What is Your Gender?", ["Male", "Female", "Other"])
age = st.select_slider("What is Your Age?", range(1,101))
hyptertension = st.radio("Hypertension?",["Yes",'No'])
heart_disease = st.radio("Heart Disease?",["Yes","No"])
ever_married = st.radio("Ever Married?",["Yes","No"])
work_type = st.selectbox("Employment Type?", ["Private Sector", "Public Sector", "Self Employed", "Parent"])
Residence_type = st.selectbox("Residence Type?", ["Urban", "Rural"])
avg_glucose_level = st.select_slider("Average Glucose Level",range(50,401))
bmi = st.select_slider("BMI", range(15,76))
smoking_status = st.selectbox("Smoking Status", ["Currently Smokes",'Previously Smoked',"Never Smoked","Not Sure"])


st.button("Asses Your Risk")