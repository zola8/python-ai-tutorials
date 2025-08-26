import logging
import sys

import uvicorn
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryPushNotificationConfigStore, InMemoryTaskStore
from a2a.types import (
    AgentCapabilities,
    AgentCard,
    AgentSkill,
)
from dotenv import load_dotenv

from agent import KaitlynAgent
from agent_executor import KaitlynAgentExecutor

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """Starts Kaitlyn's Agent server."""
    host = "localhost"
    port = 10004
    try:
        capabilities = AgentCapabilities(streaming=True, push_notifications=True)
        skill = AgentSkill(
            id="schedule_pickleball",
            name="Pickleball Scheduling Tool",
            description="Helps with finding Kaitlyn's availability for pickleball",
            tags=["scheduling", "pickleball"],
            examples=["Are you free to play pickleball on Saturday?"],
        )
        agent_card = AgentCard(
            name="Kaitlynn Agent",
            description="Helps with scheduling pickleball games",
            url=f"http://{host}:{port}/",
            version="1.0.0",
            default_input_modes=KaitlynAgent.SUPPORTED_CONTENT_TYPES,
            default_output_modes=KaitlynAgent.SUPPORTED_CONTENT_TYPES,
            capabilities=capabilities,
            skills=[skill],
        )

        # TODO wrong code with push notifications
        # httpx_client = httpx.AsyncClient()
        request_handler = DefaultRequestHandler(
            agent_executor=KaitlynAgentExecutor(),
            task_store=InMemoryTaskStore(),
            push_config_store=InMemoryPushNotificationConfigStore(),
        )
        server = A2AStarletteApplication(
            agent_card=agent_card, http_handler=request_handler
        )

        uvicorn.run(server.build(), host=host, port=port)

    except Exception as e:
        logger.error(f"An error occurred during server startup: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
