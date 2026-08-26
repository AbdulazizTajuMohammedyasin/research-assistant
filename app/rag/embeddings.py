from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


def create_embeddings():
    return GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2"
    )

#testing     
if __name__ == "__main__":
    embeddings = create_embeddings()

    vector = embeddings.embed_query(
        "What is Retrieval Augmented Generation?"
    )

    print(len(vector))
    