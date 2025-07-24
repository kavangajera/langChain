# from openai import OpenAI
from dotenv import load_dotenv
import os
from langchain_openai import OpenAI
load_dotenv()

# MODEL_SECRET_KEY = os.getenv("MISTRAL_KEY")

# client = OpenAI(
#     base_url="https://openrouter.ai/api/v1",
#     api_key=MODEL_SECRET_KEY
# )

# completion = client.chat.completions.create(

#     model="mistralai/mistral-small-3.2-24b-instruct:free",
#     messages=[
#         {
#             "role": "system",
#             "content": "You are very good and helpful geography assistant."
#         },
#         {
#             "role": "user",
#             "content": "What is the capital of France?"
#         }
#     ]
# )

# print(completion.choices[0].message.content)
# ------------------ PAID -----------------

llm = OpenAI(model="gpt-3.5-turbo", temperature=0.9, max_tokens=10)
# temperature range is 0 to 1, where 0 is deterministic and 1 is more random
# from 0 to 0.3 is used for mathematics,specialized tasks
# from 0.3 to 0.7 is used for general tasks
# from 0.7 to 1 is used for creative tasks
# from 1 to 2 for brainstorming, creative writing, etc.

result = llm.invoke("What is the capital of India?")

print(result) 

