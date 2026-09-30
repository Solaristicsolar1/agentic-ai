import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

chat_model = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=api_key,
    temperature=1.0,
)

embeddings = OllamaEmbeddings(
    model="qwen3-embedding:0.6b"
)

path = "src/Rag/basic_rag/early_human_inventions.txt"

loader = TextLoader(path)
loaded_text = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50,)
chunks = text_splitter.split_documents(loaded_text)
# print(chunks)

# vector_store = FAISS.from_documents(
#     chunks,
#     embeddings
# )

# vector_store.save_local("src/Rag/basic_rag/faiss_index")

vector_store = FAISS.load_local(
    "src/Rag/basic_rag/faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vector_store.as_retriever(search_kwargs = {"k": 1})
# response = retriever.invoke("What was the Acheulean hand axe, and what was it used for")
# print(response[0].page_content)

template = """
Answer the question using only the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

def format_doc(doc):
    return "\n\n".join([d.page_content for d in doc])

prompt = ChatPromptTemplate.from_template(template)

chain = (
    {"context": retriever | format_doc, "question": RunnablePassthrough()}
    | prompt
    | chat_model
    | StrOutputParser()
)

response = chain.invoke("What were Oldowan tools?")

print(response)


