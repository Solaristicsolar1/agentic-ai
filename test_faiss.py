import os
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_ollama import OllamaEmbeddings

embeddings_model = OllamaEmbeddings(
    model="qwen3-embedding:0.6b"
)


def main():
    path = "src/Rag/example.txt"

    text_loader = load_text(path)

    chunk_of_text = text_split(text_loader, 400, 50, "\n", len, False)

    vector_db = FAISS.from_documents(chunk_of_text, embeddings_model)
    retriever = vector_db.as_retriever(search_kwargs = {"k": 1})

    response = retriever.invoke("What were some of the earliest tools made by humans, and what materials were they made from?")
    print(response)

# Function to load text content from a file at the given path
def load_text(path: str):
    # Check if the file or directory exists at the given path
    if not os.path.exists(path):
        # Raise an error if the path is invalid or missing
        raise ValueError("Path does not exist")

    # Initialize a TextLoader instance with the provided file path
    loader = TextLoader(path)
    # Load the text content and return it (typically as a list of Document objects)
    return loader.load()

def text_split(
    text: str,
    chunk_size: int,
    chunk_overlap: int,
    separator: str,
    length_function,
    is_separator_regex: bool,
):
    text_splitter = CharacterTextSplitter(
        separator=separator,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=length_function,
        is_separator_regex=is_separator_regex,
    )

    return text_splitter.split_documents(text)

main()