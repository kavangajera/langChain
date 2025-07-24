from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
You are a helpful STEM chatbot. Answer the question based on the selected topics and explanation type.
Question: {question}
Selected Topics: {topics}
Explanation Type: {explanation_type}
""",
input_variables=["question", "topics", "explanation_type"],
validate_template=True,
)

# if template is so large then store it in different file and import it as json

template.save("stem_chatbot_template.json")