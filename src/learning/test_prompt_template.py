import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

# if api_key:
#     print("True")
# else:
#     print("False")

chat_model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=1,
    max_tokens=500
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an {role} with 50 years of experience. Don't answer anything that is not related to history, your reply should be 'out of boundary'"),
    ("human", "{explain}")
])

# message = [
#     ("system", "Act as an historian with 40 years of experience in history"),
#     ("human", "About barack obama and his life")
# ]

message = prompt.format(
    explain = "what is photosynthesis",
    role="historian"
)

# response = chat_model.invoke(message)

for chunk in chat_model.stream(message):
    print(chunk.content, end="", flush=True)

# print(response.content)

