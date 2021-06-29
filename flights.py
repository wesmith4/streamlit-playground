from os import openpty
import streamlit as st
import pandas as pd
import pydeck as pdk
from streamlit.script_runner import ScriptControlException
import numpy as np

# Data import
df = pd.read_csv('./full_routes_data.csv')
st.dataframe(df)

st.write("Distinct Airlines")
st.write(df.Airline.unique())

st.write('## Filters')
origin_countries = st.multiselect('Origin Countries',options=df.src_Country.unique())
dest_countries = st.multiselect('Destination Countries',options=df.dest_Country.unique())

st.write(origin_countries)

st.write('a' in ['a','b','c'])

# selectedData = df.loc[(df.src_Country in origin_countries) & (df.dest_Country in dest_countries)]

# df.filter()

selectedData = np.where([df.src_Country in origin_countries,df.dest_Country in dest_countries],df,-1)

coords = selectedData[['src_Longitude','src_Latitude','dest_Longitude','dest_Latitude']]


arc_layer = pdk.Layer(
    "ArcLayer",
    data=coords,
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