import datetime
import re
import streamlit as st
import requests
import pandas as pd
import numpy as np

st.markdown("<h1 style='text-align: center;'>New York Taxi Fare</h1>", unsafe_allow_html=True)

# '''
# # New York Taxi's
# '''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''
col1,col2 = st.columns(2)
with col1:
    date = st.date_input(
        "When are you leaving?",
        datetime.date(2019, 7, 6))
    st.write('Leaving date:', date)
with col2:
    time = st.time_input('What time do you want to depart?', datetime.time(8, 45))

col1,col2 = st.columns(2)
with col1:
    plon = st.number_input('Pickup longitude',value=-73.965355)
    dlong = st.number_input('Dropoff longitude',value=-73.778137)

with col2:
    plat = st.number_input('Pickup latitude',value=40.782864)
    dlat = st.number_input('Dropoff latitude',value=40.641312)

p = st.slider('Person', 1, 10, 1)


dflon = [plon,dlong]
dflat = [plat,dlat]

df = pd.DataFrame(
    {'longitude':dflon,
     'latitude':dflat}
)

st.map(df)
# if st.checkbox('Leave later'):
#     st.write(
#         t = st.time_input('What time do you want to leave?', datetime.time(8, 45))
#         )


# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# '''

# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''

datetime = str(date)+" " +str(time)
params =  {
    "pickup_datetime":datetime,
    "pickup_longitude":plon,
    "pickup_latitude":plat,
    "dropoff_longitude":dlong,
    "dropoff_latitude":dlat,
    "passenger_count":p
}

req = requests.get(url,params=params)
res = req.json()

st.subheader("$"+str(round(res["fare"],2)))
