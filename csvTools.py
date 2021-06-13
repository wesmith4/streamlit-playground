import pandas as pd
import streamlit as st

st.title('CSV Tools')

st.markdown("""
## Upload a CSV file
""")

uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("Some info about your dataframe:")

    st.dataframe(df)

    cols = df.columns
    st.write(cols)


    df[df.isna().sum(axis=1) > 0]