from app.llm.gemini import create_gemini_llm
from app.rag.retriever import get_retriever
from dotenv import load_dotenv


def answer_question(question: str):
    load_dotenv()
    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
                Answer the question using ONLY
                the provided context.

                Context:
                {context}

                Question:
                {question}
            """

    llm = create_gemini_llm()

    return llm.invoke(prompt)

#test
# if __name__ == "__main__":
#     response = answer_question(
#         "mention 3 layered archtecture of android os?"
#     )

#     print(response.text)