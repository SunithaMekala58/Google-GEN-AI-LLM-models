#Google Gen AI end to end project - text based model
# 1st project Using frontend Streamlit
import streamlit as st
import os

import pathlib
import textwrap

from IPython.display import display
from IPython.display import Markdown
#gemini 2.0.flash
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.environ['GEMINI_API_KEY'] = 'XYZ'
import google.generativeai as genai
genai.configure(api_key = os.environ['GEMINI_API_KEY'])

def get_gemini_response(question):
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title = 'GEMINI LLM APP')

st.header('Gemini AI BOT Application')

input=st.text_input("Input: ",key = "input")

submit = st.button("Click me to generate response")

if submit:
    
    response =  get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)