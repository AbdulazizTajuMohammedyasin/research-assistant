from langchain.agents import create_agent
from app.llm.gemini import create_gemini_llm

from app.tools.knowledge_base import search_knowledge_base
from app.tools.web_search import web_search

model = create_gemini_llm()

agent = create_agent(
    model=model,
    tools=[
        search_knowledge_base,
        web_search,
    ],
    system_prompt="""
            You are an AI research assistant.

            Use search_knowledge_base when the user asks
            about uploaded documents or internal knowledge.

            Use web_search for current information.

            Use both tools when comparing internal and
            external information.

            Always provide a well-structured answer.
        """,
)

