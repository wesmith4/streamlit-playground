import streamlit as st
import pandas as pd
import pydeck as pdk
from streamlit.script_runner import ScriptControlException

# Data import
coords = pd.read_csv('./full_routes_data.csv')
st.dataframe(coords)

us_data = coords.loc[(coords.src_Country == "United States") & (coords.dest_Country == "United States") & (coords.Airline == "AA")]

st.dataframe(us_data)

st.write("Distinct Airlines")
st.write(coords.Airline.unique())


arc_layer = pdk.Layer(
    "ArcLayer",
    data=us_data,
    get_source_position=["src_Longitude","src_Latitude"],
    get_target_position=["dest_Longitude","dest_Latitude"],
    get_tilt=15,
    get_source_color=[0,255,0,40],
    get_target_color=[240,100,0,40]
)

deck = pdk.Deck(
    layers=[arc_layer]
)

st.pydeck_chart(deck)