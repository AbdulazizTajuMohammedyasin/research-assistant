import os

from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore

from app.rag.embeddings import create_embeddings


def get_vector_store():
    pc = Pinecone(
        api_key=os.getenv("PINECONE_API_KEY")
    )

    index = pc.Index(
        os.getenv("PINECONE_INDEX_NAME")
    )

    return PineconeVectorStore(
        index=index,
        embedding=create_embeddings(),
    )