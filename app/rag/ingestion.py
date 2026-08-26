from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_documents(directory: str) -> list[Document]:
    documents = []

    for file_path in Path(directory).glob("*.pdf"):
        loader = PyPDFLoader(str(file_path))
        documents.extend(loader.load())

    return documents

def split_documents(documents: list[Document]) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    return splitter.split_documents(documents)

if __name__ == "__main__":
    docs = load_documents("knowledge_base")
    chunks = split_documents(docs)

    print(f"Loaded {len(docs)} documents")
    print(f"Created {len(chunks)} chunks")

    print("\nFirst chunk:\n")
    print(chunks[0].page_content)
    print(chunks[0].metadata)