import streamlit as st
import pandas as pd
import numpy as np
import json
import altair as alt
import plotly.express as px
import plotly.graph_objects as go

st.write('Testing docstring markdown:')
"""
# Header 1
## Header 2
### Header 3

"""

with st.beta_expander('Click me',):
    st.write('Using a spinner?')

X = np.arange(9).reshape((3,3))

evals,evecs = np.linalg.eig(X)

st.write(evecs)

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = px.scatter_3d(df,x='a', y='b',z='c',size_max=10)

st.write(c)

# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
z = z_data.values
st.write(z)
sh_0, sh_1 = z.shape
x, y = np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
fig.update_layout(title='Mt Bruno Elevation', autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))
st.write(fig)

x = np.arange(0,25,1)
y = np.arange(0,25,1)
x,y = np.meshgrid(x,y)
z = x**2 / y**2
st.write(z)
fig = go.Figure(data=[go.Surface(z=z,x=x,y=y)])
st.write(fig)