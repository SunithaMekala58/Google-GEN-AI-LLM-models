# Chatbot using LangChain Framework with Ollama's Deepseek-R1 Model:
In this project, I developed an interactive chatbot using the LangChain framework integrated with the Ollama's Deepseek-R1 model. This solution allows users to interact with the model through a web interface powered by Streamlit, enabling natural language understanding and step-by-step question answering. Below is an explanation of the key components of the code:

## LangChain Framework:

LangChain is a framework used to build applications that can connect to large language models (LLMs). The code uses LangChain's ChatPromptTemplate to structure the conversation prompts dynamically.
This template helps in preparing the question for the LLM by setting up the question and instructing the model to answer in a step-by-step manner.
OllamaLLM Model Integration:

The OllamaLLM class from langchain_ollama.llms is used to integrate the Deepseek-R1 model. The model generates responses to user queries based on the pre-trained data in Deepseek-R1.
This integration allows the code to invoke the model and get the appropriate answer based on the user’s question.
Streamlit Web Application:

Streamlit is a popular tool to quickly build interactive web applications. Here, it’s used to create a simple web interface where users can input their questions and receive answers from the model.
st.title(): Sets the title of the app ("My ChatBot using Deepseek-R1").
st.text_input(): Creates an input box where users can type their question.
st.write(): Displays the response from the model or any error messages.

## Question Answering Logic:
The code accepts a question from the user and formats it using the ChatPromptTemplate.
It then invokes the chain (which is a combination of the prompt and the model) to generate a response from the Deepseek-R1 model.
If the model returns an answer, it is displayed on the web interface.
If there is an error, the system captures it and displays an appropriate error message using a try-except block.

## Skills & Technologies Used:
LangChain for prompt management and chaining of model calls.
Ollama's Deepseek-R1 for natural language processing (NLP) and question answering.
Streamlit for creating an interactive web-based interface.
Python for coding, data processing, and managing interactions between the components.

This project demonstrates my ability to combine various tools in Python for building NLP applications and interactive web interfaces, using modern frameworks such as LangChain and Streamlit.

