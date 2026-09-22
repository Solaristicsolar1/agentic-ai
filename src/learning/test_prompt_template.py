import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

chat_model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=1,
    max_tokens=500
)