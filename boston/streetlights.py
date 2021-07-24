from pydeck.bindings.map_styles import DARK
import streamlit as st
import pandas as pd
import pydeck as pdk

@st.cache
def getData(URL):
    return pd.read_csv(URL)

data = getData('https://data.boston.gov/dataset/52b0fdad-4037-460c-9c92-290f5774ab2b/resource/c2fcc1e3-c38f-44ad-a0cf-e5ea2a6585b5/download/streetlight-locations.csv')

streetlights = pdk.Layer(
    'HeatmapLayer',
    data=data,
    get_position=['Long','Lat'],
    opacity=0.9,
    threshold=0.75,
)

deck = pdk.Deck(
    layers=[streetlights],
    map_style=DARK
)

st.pydeck_chart(deck)