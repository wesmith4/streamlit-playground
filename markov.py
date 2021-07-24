import streamlit as st
import numpy as np

st.write('## Create your transition matrix:')

text_input = st.text_area('Transition Matrix',help="Separate entries by commas, rows by semicolons")

if text_input is not None:
    A = np.matrix(text_input)
    st.code(A)


    
nrows = st.number_input('Number of rows',min_value=1,max_value=5,step=1)
ncols = st.number_input('Number of columns',min_value=1,max_value=5,step=1)

Transition_Matrix = np.zeros((nrows, ncols))


for r in range(nrows):
    for c in range(ncols):
        Transition_Matrix[r,c] = st.number_input(label='Val')