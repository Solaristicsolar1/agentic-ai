import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import FewShotChatMessagePromptTemplate, ChatPromptTemplate

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

chatModel = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=api_key,
    temperature=0.9,
    max_tokens=500
)

examples = [
    {
        "question": "What is Amazon S3?",
        "answer": """Amazon S3 is an object storage service.

Think of it like a highly durable storage system where you can store
files such as images, videos, backups, and documents.

Scenario:
A photo-sharing application can store uploaded images in an S3 bucket.

Security:
Keep the bucket private by default and use IAM policies or
presigned URLs to control access.

Cost:
You generally pay for the storage you use and related requests/data transfer."""
    },

    {
        "question": "What is Amazon EC2?",
        "answer": """Amazon EC2 provides virtual servers in AWS.

Think of it like renting a computer in the AWS cloud instead of
buying a physical server.

Scenario:
An application can run its backend API on an EC2 instance.

Security:
Use security groups to control network traffic and IAM roles
instead of putting AWS credentials on the server.

Cost:
You pay for the compute capacity you use, with different pricing
options depending on how you run the instances."""
    },

    {
        "question": "What is Amazon VPC?",
        "answer": """Amazon VPC lets you create a logically isolated network
inside AWS.

Think of it like creating your own private network in the cloud.

Scenario:
You can place application servers in private subnets and expose
only an Application Load Balancer to the internet.

Security:
Use security groups and network ACLs to control traffic.

Cost:
The VPC itself is generally not charged, but resources and
networking components you deploy around it can incur charges."""
    }
]

example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{question}"),
    ("ai", "{answer}")
])

few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_prompt
)

final_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are an AWS cloud instructor.

Your job is to teach AWS concepts clearly to learners.

For AWS service questions:
1. Explain what the service is.
2. Give a simple mental model.
3. Give a practical scenario.
4. Explain important security considerations.
5. Explain relevant cost considerations.

Use simple language and teach the reasoning behind AWS architecture.
Do not invent AWS features."""
    ), few_shot_prompt,
    ("human", "{question}")
])

question = input("Input your question: ").strip()

chain = final_prompt | chatModel

for chunk in chain.stream({
    "question": question
}):
    print(chunk.content, end="", flush=True)

