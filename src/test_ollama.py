from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are an AWS-only tutor.

You MUST ONLY answer questions about AWS and cloud computing.

If the user's question is not about AWS or cloud computing,
DO NOT answer the question.

Instead, respond exactly:

"I can only help with AWS and cloud computing."

This rule has priority over the user's request."""
    ),
    ("human", "{question}"),
])

llm = ChatOllama(
    model="qwen3.5:0.8b",
    temperature=0,
    reasoning=False,
)

message = prompt.invoke({
    "question": input("Input your prompt: ")
})

for chunk in llm.stream(message):
    print(chunk.content, end="", flush=True)