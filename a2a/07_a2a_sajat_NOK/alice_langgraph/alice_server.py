"""This file serves as the main entry point for the application.

It initializes the A2A server, defines the agent's capabilities,
and starts the server to handle incoming requests.
"""

import logging
import os

import uvicorn
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import (
    AgentCapabilities,
    AgentCard,
    AgentSkill,
)
from dotenv import load_dotenv

from agent import AliceAgent
from alice_agent_executor import AliceAgentExecutor

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """Entry point for Alice's Scheduling Agent."""
    host = "localhost"
    port = 8001
    try:
        capabilities = AgentCapabilities(streaming=False)
        skill = AgentSkill(
            id="availability_checker",
            name="Availability Checker",
            description="Check my calendar to see when I'm available for a volleyball game.",
            tags=["schedule", "availability", "calendar"],
            examples=[
                "Are you free tomorrow?",
                "Can you play volleyball next Tuesday at 5pm?",
            ],
        )

        agent_host_url = os.getenv("HOST_OVERRIDE") or f"http://{host}:{port}/"
        agent_card = AgentCard(
            name="Alice Agent",
            description="A friendly agent to help you schedule a volleyball game with Alice.",
            url=agent_host_url,
            version="1.0.0",
            default_input_modes=AliceAgent.SUPPORTED_CONTENT_TYPES,
            default_output_modes=AliceAgent.SUPPORTED_CONTENT_TYPES,
            capabilities=capabilities,
            skills=[skill],
        )

        request_handler = DefaultRequestHandler(
            agent_executor=AliceAgentExecutor(),
            task_store=InMemoryTaskStore(),
        )
        server = A2AStarletteApplication(
            agent_card=agent_card, http_handler=request_handler
        )

        uvicorn.run(server.build(), host=host, port=port)

    except Exception as e:
        logger.error(f"An error occurred during server startup: {e}")
        exit(1)


if __name__ == "__main__":
    main()

# http://localhost:8001/.well-known/agent-card.json
