import streamlit as st
import numpy as np
# from handcalcs.handcalcs import handcalc

# st.write('## Create your transition matrix:')

# text_input = st.text_input('Transition Matrix',help="Separate entries by commas, rows by semicolons")

# if text_input is not None:
#     A = np.matrix(text_input)
#     st.code(A)
#     st.write('{} by {} transition matrix:'.format(np.shape(A)[0],np.shape(A)[1]))

#     np.shape(A)

#     # st.latex(f"{}x^2 + {b}x + {c} = 0")


# st.latex(r"""\bold{A}""")

st.metric(label="Value", value=.87, delta=.01)


st.date_input()