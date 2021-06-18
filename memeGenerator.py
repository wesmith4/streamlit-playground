import streamlit as st
import requests
import json
from PIL import Image

@st.cache
def getImageOptions():
    url = "https://ronreiter-meme-generator.p.rapidapi.com/images"

    headers = {
        'x-rapidapi-key': "08971bf610msh534f3670df11ca3p19b660jsna1e647c64610",
        'x-rapidapi-host': "ronreiter-meme-generator.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    return json.loads(response.text)

@st.cache
def getFontOptions():
    url = "https://ronreiter-meme-generator.p.rapidapi.com/fonts"

    headers = {
        'x-rapidapi-key': "08971bf610msh534f3670df11ca3p19b660jsna1e647c64610",
        'x-rapidapi-host': "ronreiter-meme-generator.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    return json.loads(response.text)


@st.cache
def generateMeme(image,font,topText,bottomText):
    url = "https://ronreiter-meme-generator.p.rapidapi.com/meme"

    querystring = {"meme":image,"bottom":bottomText,"top":topText,"font":font,"font_size":"50"}

    headers = {
        'x-rapidapi-key': "08971bf610msh534f3670df11ca3p19b660jsna1e647c64610",
        'x-rapidapi-host': "ronreiter-meme-generator.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)

    return response.text


imageOptions = getImageOptions()
fontOptions = getFontOptions()

image = st.selectbox("Choose a meme image:",options=imageOptions)
font = st.selectbox("Choose a font",options=fontOptions)
topText = st.text_input(label="Top Text")
bottomText = st.text_input(label="Bottom Text")

meme = generateMeme(image=image,font=font,topText=topText,bottomText=bottomText)
st.write(type(meme))

st.write(Image.frombytes(mode="P",size=(400,400),data=bytearray(meme)))

