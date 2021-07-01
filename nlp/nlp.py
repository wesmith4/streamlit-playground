from typing import ForwardRef
import nltk
from nltk.corpus import stopwords
import streamlit as st
import urllib.request
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


# NLP Example using SpaceX on Wikipedia

URL = "https://wikipedia.org/wiki/spacex"


@st.cache
def getHTML(url):
    response = urllib.request.urlopen(url)
    return response.read()

html = getHTML(URL)
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
# st.write(text)

tokens = [t for t in text.split()]
st.write(tokens)

sr = stopwords.words('english')

clean_tokens = tokens[:]

for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)

print(freq.items()