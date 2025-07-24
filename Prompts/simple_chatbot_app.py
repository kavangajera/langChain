from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-Coder-480B-A35B-Instruct",
    task="text-generation"
)

st.header("Simple Chatbot App")
st.write("This is a simple chatbot app using LangChain and HuggingFace.")

user_input = st.text_input('Enter your prompt:')

if st.button('Submit'):
    if user_input:
        chat = ChatHuggingFace(llm=llm)
        response = chat.invoke(user_input)
        st.write("Response from the model:")
        st.write(response.content)
    else:
        st.write("Please enter a prompt before submitting.")

