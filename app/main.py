from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

print("1. Creating LLM...")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0,
)

print("2.LLM created")

response = llm.invoke("Explain RAG in one paragraph.")

print("3.Response received")
print(response.text)