from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv
import os
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-Coder-480B-A35B-Instruct",
    task="text-generation"
)

st.header("STEM Chatbot App")
st.write("This is a simple chatbot application that uses a language model to answer questions related to STEM topics.")

stem_topics = st.sidebar.multiselect(
    'Select Topics',
    options=['Technology', 'Science', 'Health', 'Education', 'Environment'],
    default=['Technology']
)

explaination_type = st.sidebar.selectbox(
    'Select Explanation Type',
    options=['Mathematical', 'Summary', 'Using Example'],
    index=0
)

question = st.text_input("Enter your question:")

template = load_prompt("stem_chatbot_template.json")

model = ChatHuggingFace(llm=llm)




if st.button('Submit'):
    try:
        if not question:
            st.error("Please enter a question.")
        elif not stem_topics:
            st.error("Please select at least one topic.")
        elif not explaination_type:
            st.error("Please select an explanation type.")
        else:
            chain = template | model
            
            response = chain.invoke({
                "question": question,
                "topics": ", ".join(stem_topics),
                "explanation_type": explaination_type
            })
            st.write("Response from the model:")
            st.write(response.content)
    except Exception as e:
        st.error(f"An error occurred: {e}")

# without using chain
# prompt = template.invoke({
#     "question": question,
#     "topics": ", ".join(stem_topics), 
#     "explanation_type": explaination_type
# })
# st.write("Response from the model:")
# st.write(response.content)

# response = model.invoke(prompt)

# twice invoke is not needed, first invoke is for prompt and second is for model

