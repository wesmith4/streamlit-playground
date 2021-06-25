from requests.models import Response
import streamlit as st
import requests
# from urllib.parse import urlparse

st.title("Word Info")

word = st.text_input("Type a word")

if word is not None:
    url = "https://wordsapiv1.p.rapidapi.com/words/{}/also".format(word)

    headers = {
        'x-rapidapi-key': "08971bf610msh534f3670df11ca3p19b660jsna1e647c64610",
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    st.write(response.text)


