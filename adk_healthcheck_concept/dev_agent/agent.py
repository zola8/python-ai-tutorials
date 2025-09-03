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
    You are the healthcheck manager for an application.
    The application runs on some environment:
    - DEV
    - PROD

    The application has the following components:
    - frontend
    - backend
    
    The user can ask you to perform a health check, but both the environment and the component should be selected.
    Use your best judgement to determine which environment and component the user is referring to.
    
    If a health check happened and an issue was found, offer to the user to open an incident ticket about it.
    You must provide the relevant information what you got from the health check.

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
