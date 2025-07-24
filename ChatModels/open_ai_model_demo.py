from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_SECRET_KEY = os.getenv("OPENAI_API_KEY")
client = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.9,
    max_tokens=10,
    api_key=MODEL_SECRET_KEY
)
completion = client.invoke(
    "What is the capital of France?",
    system_message="You are a helpful geography assistant."
)   
print(completion.content)