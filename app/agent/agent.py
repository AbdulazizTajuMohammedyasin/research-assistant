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
    system_prompt = """
        You are an AI research assistant.

        You have access to two tools:

        1. search_knowledge_base:
        The knowledge base contains the user's uploaded PDFs,
        lecture notes, course materials, documentation,
        and private documents.

        ALWAYS search the knowledge base first when a question
        could reasonably be answered from those documents.

        2. web_search:
        Search the web for current or external information.

        When answering:

        - Use the knowledge base when the information may be available there.
        - Use web search when current or external information is required.
        - Use both when appropriate.
        - Cite information from the sources you used.
        - Use numbered citations such as [1], [2], [3].
        - Include a "Sources" section at the end of your answer.
        - Do not invent citations or sources.
        - Only cite sources returned by the tools.
        """
        )

