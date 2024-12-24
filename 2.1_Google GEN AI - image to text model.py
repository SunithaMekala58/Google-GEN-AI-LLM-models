#Google Gen AI end to end project - Multimodel based
# 2nd project using frontend Streamlit
import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image

import os
os.environ['GEMINI_API_KEY'] = 'XYZ'

import google.generativeai as genai
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

## Function to load google model and get response

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title=" Image CREATION App")

st.header("Gemini AI IMAGE APP")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""  
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Explain me about the image")

## If ask button is clicked

if submit:
   
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)