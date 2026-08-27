from app.rag.retriever import get_retriever
from dotenv import load_dotenv
load_dotenv()

def search_knowledge_base(query: str) -> str:
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

#print(search_knowledge_base("Androidmanifest"))