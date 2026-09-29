import os
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings


embeddings = OllamaEmbeddings(
    model="qwen3-embedding:0.6b"
)


def main():
    path = "src/Rag/example.txt"
    result = load_text(path)
    # print(result)
    # text = text_split(result[0].page_content, 1000, 200, "\n", len, False)

    # print(text[0], len(text[0]))

    recursive = recursive_text_splitter(result[0].page_content, 800, 50)
    print(len(recursive))

    # print(recursive[0], "\n\n", recursive[1])

    vector = embeddings.embed_query(
        "What is Amazon EC2?"
    )

    print(len(vector))
    print(vector[:5])

def load_text(path:str):
    if not os.path.exists(path):
        raise ValueError("Path does not exist")

    loader = TextLoader(path)
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

def recursive_text_splitter(text: str, chunk_size: int, chunk_overlap: int):
    recursive_split = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    return recursive_split.split_text(text)


def chroma_db_store(embedding_model: str, chunks: str):


main()
