from dotenv import load_dotenv

from app.llm.gemini import create_gemini_llm
from app.chat.conversation import Conversation


def main():
    load_dotenv()

    llm = create_gemini_llm()
    conversation = Conversation()

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
        
        conversation.add_user_message(question)
        response = llm.invoke(conversation.get_messages())
        conversation.add_ai_message(response.text)

        print(f"\nAI: {response.text}\n")


if __name__ == "__main__":
    main()