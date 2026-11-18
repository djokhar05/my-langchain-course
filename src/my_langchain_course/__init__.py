from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from tavily import TavilyClient

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search results
    """
    print(f"Searching for: {query}")
    return tavily.search(query=query)

llm = ChatGroq(model="openai/gpt-oss-120b")
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main() -> None:
    print("Hello from my-langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="Search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details")})
    print(result)


if __name__ == "__main__":
    main()