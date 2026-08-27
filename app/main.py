from dotenv import load_dotenv
from app.chat.conversation import Conversation



def main():
    load_dotenv()
    from app.agent.agent import agent
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
        response = agent.invoke({"messages": conversation.get_messages()})
        ai_message = response["messages"][-1]
        text = ai_message.content[0]["text"]
        conversation.add_ai_message(text)
        print(f"\nAI: {text}\n")


if __name__ == "__main__":
    main()