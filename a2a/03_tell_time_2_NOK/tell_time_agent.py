from datetime import datetime

from a2a.types import AgentCapabilities, AgentCard, AgentSkill, TransportProtocol
from google.adk.agents import LlmAgent

TELLTIME_AGENT_INSTRUCTIONS = """
You are a TellTime Agent.

## Core Behavior:
- tell the current time using your tool
- don't do anything else. If the question is not about to know the time, tell: 'I don't know the answer'
"""


def current_time_tool():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_telltime_agent(model: str) -> LlmAgent:
    return LlmAgent(
        model=model,
        name="telltime_agent",
        description="An AI agent which tells the current time",
        instruction=TELLTIME_AGENT_INSTRUCTIONS,
        tools=[current_time_tool],
    )


def get_telltime_agent_card(agent_url: str) -> AgentCard:
    return AgentCard(
        name="TellTime Agent",
        description="TellTime Agent to tell the time",
        url=agent_url,
        version="1.0",
        capabilities=AgentCapabilities(streaming=True),
        default_input_modes=["text/plain"],
        default_output_modes=["text/plain"],
        preferred_transport=TransportProtocol.jsonrpc,
        skills=[
            AgentSkill(
                id="telltime_agent",
                name="TellTime Agent",
                description="TellTime Agent",
                tags=["tell time"],
            )
        ],
    )
