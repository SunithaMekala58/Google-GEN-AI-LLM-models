# Project using langchain framework - using ollama - deepseek-r1 model
# pip install -upgrade langchain langchain-community
# pip install -U langchain-ollama
# pip install streamlit

from langchain.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

import streamlit as st

st.title("My ChatBot using Deepkseek-R1")

template = """question: {question}
Answer = Generate the answer step by step"""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model = "deepseek-r1")

chain = prompt | model

question = st.text_input("Enter you question here:")

if  question:
     try: 
         formatted_prompt = prompt.format(question=question)
        
         response = chain.invoke({"question":question})
        
         #print("Response: ",response)
         st.write(response)
         
     except Exception as e:
         #print(f"Error: {e}")
         st.write(f"Error: {e}")