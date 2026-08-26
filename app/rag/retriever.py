from app.rag.vector_store import get_vector_store


def get_retriever():
    vector_store = get_vector_store()

    return vector_store.as_retriever(
        search_kwargs={"k": 4}
    )
    
# test 
# from dotenv import load_dotenv
# load_dotenv()
# retriever = get_retriever()
# results = retriever.invoke(
#     "what are the elements of android studio?"
# )
# for doc in results:
#     print("=" * 50)
#     print(doc.page_content)