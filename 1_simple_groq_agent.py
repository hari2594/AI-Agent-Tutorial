from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()
agent = Agent(model=Groq(id="llama-3.1-70b-versatile"))

agent.print_response("write 2 sentence poem for the love between a llama and a human")