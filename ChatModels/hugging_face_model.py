from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-Coder-480B-A35B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm,temperature=1.2,max_tokens=50)

result = model.invoke(
    "Write poem on cricket.",
)
print(result.content)