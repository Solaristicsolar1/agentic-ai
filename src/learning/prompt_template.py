from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
import os
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

llm_model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=1,
    max_tokens=500
)

# llm_model2 = ChatOllama(
#     model="qwen3.5:0.8b",
#     temperature=0,
#     reasoning=False
# )

# response1 = llm_model.invoke("What is photosynthesis")
# response2 = llm_model2.invoke("What is RAG?")

# print(response1.content)
# print(response2.content)

message = [
    ("system", "Act as an historian with 20 years experience and ability to make history fun and do not answer any question that is not related to history, if asked your reply should be 'Not in my knowledge base'"),
    ("human","What is photosynthesis"),
]

for chunk in llm_model.stream(
    message
):
    print(chunk.content, end="", flush=True)