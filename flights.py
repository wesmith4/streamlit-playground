import streamlit as st
import pandas as pd
import pydeck as pdk
from streamlit.script_runner import ScriptControlException

# Data import
routes = pd.read_csv('./routes.csv')

st.dataframe(routes)


st.dataframe(routes.isna())


# arc_layer = pdk.Layer(
#     "ArcLayer",
#     data=routes[['src_Longitude','src_Latitude','dest_Longitude','dest_Latitude']],
#     get_source_position=["src_Longitude","src_Latitude"],
#     get_target_position=["dest_Longitude","dest_Latitude"],
#     get_tilt=15,
#     get_source_color=[0,255,0,40],
#     get_target_color=[240,100,0,40]
# )

# deck = pdk.Deck(
#     layers=[arc_layer]
# )

# st.pydeck_chart(deck)