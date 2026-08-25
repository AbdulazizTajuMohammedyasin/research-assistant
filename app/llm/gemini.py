from langchain_google_genai import ChatGoogleGenerativeAI


def create_gemini_llm() -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model="gemini-3.5-flash",
        temperature=0,
    )