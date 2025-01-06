from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.playground import Playground, serve_playground_app
from phi.tools.googlesearch import GoogleSearch

load_dotenv()

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.2-1b-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

# Agent for searching Google for healthcare-related information
google_search_agent = Agent(
    name="Google Finance Agent",
    description="Searches Google for Finance related information.",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[GoogleSearch()],
    instructions=[
        "Retrive finance information from the trusted source"
    ],
    show_tool_calls=True,
    debug_mode=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id="llama-3.2-1b-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)



app = Playground(agents=[web_agent, google_search_agent, finance_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)