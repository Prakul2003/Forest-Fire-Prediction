import streamlit as st
import joblib
import pickle
import sklearn
from sklearn.tree import DecisionTreeClassifier
import numpy as np

model=joblib.load('model.pkl')
def recommend(input):
    pass

st.title("Forest Fire Prediction")
st.number_input("Temperature[C]",value=28)
st.number_input("Humidity[%]",min_value=0.0,max_value=100.0,value=44.71)
st.number_input("TVOC[ppb]",min_value=0,max_value=600000,value=174)
# st.number_input("eCO2[ppm]",min_value=0,max_value=600000,value=426)
st.number_input("Raw H2",min_value=10000,max_value=130000,value=12774)
st.number_input("Raw Ethanol",min_value=15000,max_value=250000,value=20548)
st.number_input("Pressure[hPa]",min_value=925.0,max_value=940.0,value=937.408)
# st.number_input("PM1.0",min_value=0.0,max_value=35000.0,value=1.68)
st.number_input("NC2.5",min_value=0.0,max_value=35000.0,value=.041)
# st.number_input("CNT",value=2849)

if(st.button("PREDICT")):
    print()