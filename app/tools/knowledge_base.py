from langchain.tools import tool
from app.rag.retriever import get_retriever

@tool
def search_knowledge_base(query: str) -> list:
    """Search the user's knowledge base for relevant information."""
    retriever = get_retriever()
    docs = retriever.invoke(query)
    results = []
    for doc in docs:
        results.append(
        {
            "content": doc.page_content,
            "source": doc.metadata.get("source"),
            "page": doc.metadata.get("page"),
        }
    )
    return results

