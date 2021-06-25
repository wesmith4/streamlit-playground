import streamlit as st
import pandas as pd
import pydeck as pdk

# Data imports

airlines = pd.read_csv('./data/airlines.csv')
airplanes = pd.read_csv('./data/airplanes.csv')
airports = pd.read_csv('./data/airports.csv')
routes = pd.read_csv('./data/routes.csv')


st.write("## Airlines")
st.dataframe(airlines)

st.write('## Airplanes')
st.dataframe(airplanes)

st.write("## Airports")
st.dataframe(airports)

st.write('## Routes')
st.dataframe(routes)

airport_locations = airports[['Airport ID', 'Latitude', 'Longitude']].copy()

routes['lat_beg'] = routes['Source airport ID'].apply(lambda x: airports[airports['Airport ID'] == x][['Latitude']])

st.write(routes)