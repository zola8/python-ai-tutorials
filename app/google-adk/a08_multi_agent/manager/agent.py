# https://github.com/bhancockio/agent-development-kit-crash-course/tree/main/7-multi-agent
# https://youtu.be/P4VFL9nIaIA?si=EUna5EysJrxaNyhW&t=5457
# https://github.com/ollama/ollama/issues/10255#issuecomment-2800188768 -- common issue
# https://github.com/google/adk-python/issues/376
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.funny_nerd.agent import funny_nerd
from .sub_agents.news_analyst.agent import news_analyst
from .sub_agents.stock_analyst.agent import stock_analyst
from .tools.tools import get_current_time

load_dotenv()

root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="Manager agent",
    instruction="""
    You are a manager agent that is responsible for overseeing the work of the other agents.

    Always delegate the task to the appropriate agent. Use your best judgement 
    to determine which agent to delegate to.

    You are responsible for delegating tasks to the following agent:
    - stock_analyst
    - funny_nerd

    You also have access to the following tools:
    - news_analyst
    - get_current_time
    """,
    sub_agents=[stock_analyst, funny_nerd],
    tools=[
        AgentTool(news_analyst),
        get_current_time,
    ],
)
