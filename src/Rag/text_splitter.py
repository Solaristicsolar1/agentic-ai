import os
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings


embeddings_model = OllamaEmbeddings(
    model="qwen3-embedding:0.6b"
)


def main():
    path = "src/Rag/example.txt"
    result = load_text(path)
    # text = text_split(result[0].page_content, 1000, 200, "\n", len, False)

    text = result[0].page_content

    recursive = recursive_text_splitter(text, 800, 50)
    # print(len(recursive))
    # print(recursive)

    vector_db = chroma_db_store(recursive, embeddings_model)

    question = "What were some of the earliest tools made by humans, and what materials were they made from?"
    response = vector_db.similarity_search(question, k =1)
    print(response[0].page_content)


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


# Function to split a raw text string into smaller chunks using recursive character splitting
def recursive_text_splitter(text: str, chunk_size: int, chunk_overlap: int):
    # Initialize a RecursiveCharacterTextSplitter with the specified chunk size and overlap
    recursive_split = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    # Split the input text into chunks and return the resulting list of text strings
    return recursive_split.split_text(text)


# Function to store document chunks into a Chroma vector database using the given embedding model
def chroma_db_store(chunks: str, embedding_model: str):
    # Create a Chroma vector store from the provided chunks using the embedding model
    vector_store = Chroma.from_texts(chunks, embedding_model)
    # Return the created vector store instance
    return vector_store

main()
