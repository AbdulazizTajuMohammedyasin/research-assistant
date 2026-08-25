from dotenv import load_dotenv

from app.llm.gemini import create_gemini_llm


def main():
    load_dotenv()

    llm = create_gemini_llm()

    print("\nAI Research Assistant")
    print("Type 'exit' to quit.\n")
    print("=" * 100)

    while True:
        question = input("You: ").strip()

        if question.lower() == "exit":
            print("Goodbye!")
            break

        if not question:
            continue

        response = llm.invoke(question)

        print(f"\nAI: {response.text}\n")


if __name__ == "__main__":
    main()