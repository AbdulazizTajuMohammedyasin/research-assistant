from langchain.tools import tool
from langchain_community.utilities import SerpAPIWrapper


search = SerpAPIWrapper()

@tool
def web_search(query: str) -> str:
    """Search the web for up-to-date information."""
    return search.run(query)