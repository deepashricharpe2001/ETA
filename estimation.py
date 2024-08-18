import streamlit as st
import pandas as pd 
import sklearn
from sklearn.linear_model import LinearRegression
import pickle 

# Display the logo and title
st.image('logo.png')
st.title('ETA PROJECT')

# Load the trained model (make sure the model file is named correctly)
model = pickle.load(open('estimator.pkl', 'rb'))

# User input fields
start_lat = st.number_input('Enter the value of start latitude:')
start_lng = st.number_input('Enter the value of start longitude:')
end_lat = st.number_input('Enter the value of end latitude:')
end_lng = st.number_input('Enter the value of end longitude:')
distance_km = st.number_input('Enter the value of distance (km):')
traffic_density = st.number_input('Enter the value of traffic density:')
weather = st.text_input('Enter the value of weather condition:', value='rainy')
day_of_week = st.number_input('Enter the day of the week:')
hour_of_day = st.number_input('Enter the hour of the day:')

# Convert weather condition to numerical
weather_numerical = 1 if weather == 'rainy' else 2 if weather == 'foggy' else 3

# Prediction and output
if st.button('Submit'):
    time = model.predict([[start_lat, start_lng, end_lat, end_lng, distance_km, traffic_density, weather_numerical, day_of_week, hour_of_day]])[0]
    st.write(f'Estimated time of arrival: {time} minutes')
