from langchain_core.messages import AIMessage, HumanMessage


class Conversation:
    def __init__(self):
        self.messages = []

    def add_user_message(self, content: str):
        self.messages.append(HumanMessage(content=content))

    def add_ai_message(self, content: str):
        self.messages.append(AIMessage(content=content))

    def get_messages(self):
        return self.messages