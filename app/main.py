from dotenv import load_dotenv
from app.llm.gemini import create_gemini_llm


load_dotenv()

print("Creating LLM...")

llm = create_gemini_llm()

print("LLM created")

response = llm.invoke("Explain RAG in one paragraph.")

print("Response received")
print(response.text)