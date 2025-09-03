from dotenv import load_dotenv
from google.adk import Agent

from .sub_agents.incident_handling.agent import incident_handling_agent
from .tools.tools import healthcheck_backend, healthcheck_frontend

load_dotenv()

root_agent = Agent(
    model="gemini-2.0-flash",
    name="dev_agent",
    description="You are helpful assistant.",
    instruction="""
    You are the healthcheck manager for the Bazaar application.
    The application has the following components:
    - frontend
    - backend

    Always delegate the task to the appropriate agent. Use your best judgement to determine which agent to delegate to.
    Available agents:
    - incident_handling_agent

    You also have access to the following tools:
    - healthcheck_frontend
    - healthcheck_backend
    """,
    sub_agents=[
        incident_handling_agent,
    ],
    tools=[
        healthcheck_backend,
        healthcheck_frontend,
    ],
)
