'''
The idea of the agent is to teach a topic in a very simple way
'''
from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.newspaper4k import Newspaper4k

load_dotenv()


agent = Agent(
    model = Groq(id="llama-3.2-1b-preview"),
    tools=[DuckDuckGo(), Newspaper4k()],
    description="You are an experienced teacher. Explain the given topic in simple English, using clear examples to help learners understand easily.",
    instructions=[
        "For a given topic, search for the top 5 links.",
        "Then read each URL and extract the article text, if a URL isn't available, ignore it.",
        "Analyse and Extract key points and combine them into a simplified explanation.",
        "Provide a short summary as a story or example to help learners understand the topic."
    ],
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    # debug_mode=True,
)

agent.print_response("World War 1", stream=True)