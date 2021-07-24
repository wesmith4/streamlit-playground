from pydeck.bindings.map_styles import LIGHT
import streamlit as st
import pydeck as pdk
import json


# geojson = json.load('./data/ZIP_Codes.geojson')

geojsonLayer = pdk.Layer(
    'GeoJsonLayer',
    data='./data/ZIP_Codes.geojson',
    pickable=True,
)

deck = pdk.Deck(
    map_style=LIGHT,
    layers=[geojsonLayer]
)

st.pydeck_chart(deck)
