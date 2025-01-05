# from phi.agent import Agent
# from phi.model.groq import Groq
# from dotenv import load_dotenv
# from phi.tools.duckduckgo import DuckDuckGo
# from phi.tools.wikipedia import WikipediaTools
# from phi.tools.newspaper4k import Newspaper4k

# load_dotenv()
# web_agent = Agent(
#     name = 'Web Agent',
#     model = Groq(id="llama-3.1-70b-versatile"),
#     tools=[DuckDuckGo(), Newspaper4k()],
#     description="You are a senior NYT researcher writing an article on a topic.",
#     instructions=[
#         "For a given topic, search for the top 5 links.",
#         "Then read each URL and extract the article text, if a URL isn't available, ignore it.",
#         "Analyse and prepare an NYT worthy article based on the information.",
#     ],
#     show_tool_calls=True,
#     markdown=True
# )

# web_agent.print_response("Simulation theory", stream=True)

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.newspaper4k import Newspaper4k
from dotenv import load_dotenv


load_dotenv()

agent = Agent(
    model = Groq(id="llama-3.2-1b-preview"),
    tools=[DuckDuckGo(), Newspaper4k()],
    description="You are a senior NYT researcher writing an article on a topic.",
    instructions=[
        "For a given topic, search for the top 5 links.",
        "Then read each URL and extract the article text, if a URL isn't available, ignore it.",
        "Analyse and prepare an NYT worthy article based on the information.",
    ],
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    # debug_mode=True,
)
agent.print_response("Simulation theory", stream=True)