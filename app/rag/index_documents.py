from dotenv import load_dotenv

from app.rag.ingestion import (
    load_documents,
    split_documents,
)
from app.rag.vector_store import get_vector_store


def main():
    load_dotenv()

    docs = load_documents("knowledge_base")
    chunks = split_documents(docs)

    vector_store = get_vector_store()

    vector_store.add_documents(chunks)

    print(
        f"Indexed {len(chunks)} chunks."
    )


if __name__ == "__main__":
    main()