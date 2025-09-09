import asyncio
import json
import logging
from datetime import datetime
from typing import List

import httpx
import nest_asyncio
from a2a.client import A2ACardResolver
from a2a.types import AgentCard
from dotenv import load_dotenv
from google.adk import Agent
from google.adk.agents.readonly_context import ReadonlyContext

from .remote_agent_connection import RemoteAgentConnections

load_dotenv()
LOGGER = logging.getLogger(__name__)  # Get a logger instance
nest_asyncio.apply()


class HostAgent:
    """The Host agent."""

    def __init__(self, remote_agent_addresses: List[str]):
        self.agents: str = ""
        self.remote_agent_addresses = remote_agent_addresses
        self.remote_agent_connections: dict[str, RemoteAgentConnections] = {}
        self.cards: dict[str, AgentCard] = {}
        self._agent = self.create_agent()

    def create_agent(self) -> Agent:
        return Agent(
            model="gemini-2.5-flash",
            name="host_agent",
            instruction=self.root_instruction,
            description="This Host agent orchestrates scheduling pickleball with friends.",
            # tools=[
            # self.send_message,
            # book_pickleball_court,
            # list_court_availabilities,
            # ],
        )

    def root_instruction(self, context: ReadonlyContext) -> str:
        return f"""
        **Role:** You are the Host Agent, an expert scheduler for pickleball games. Your primary function is to coordinate with friend agents to find a suitable time to play and then book a court.

        **Core Directives:**

        *   **Initiate Planning:** When asked to schedule a game, first determine who to invite and the desired date range from the user.
        *   **Task Delegation:** Use the `send_message` tool to ask each friend for their availability.
            *   Frame your request clearly (e.g., "Are you available for pickleball between 2024-08-01 and 2024-08-03?").
            *   Make sure you pass in the official name of the friend agent for each message request.
        *   **Analyze Responses:** Once you have availability from all friends, analyze the responses to find common timeslots.
        *   **Check Court Availability:** Before proposing times to the user, use the `list_court_availabilities` tool to ensure the court is also free at the common timeslots.
        *   **Propose and Confirm:** Present the common, court-available timeslots to the user for confirmation.
        *   **Book the Court:** After the user confirms a time, use the `book_pickleball_court` tool to make the reservation. This tool requires a `start_time` and an `end_time`.
        *   **Transparent Communication:** Relay the final booking confirmation, including the booking ID, to the user. Do not ask for permission before contacting friend agents.
        *   **Tool Reliance:** Strictly rely on available tools to address user requests. Do not generate responses based on assumptions.
        *   **Readability:** Make sure to respond in a concise and easy to read format (bullet points are good).
        *   Each available agent represents a friend. So Bob_Agent represents Bob.
        *   When asked for which friends are available, you should return the names of the available friends (aka the agents that are active).

        **Today's Date (YYYY-MM-DD):** {datetime.now().strftime("%Y-%m-%d")}

        <Available Agents>
        {self.agents}
        </Available Agents>
        """

    async def check_remote_agent_connections(self):
        LOGGER.info('Checking remote connections...')
        async with httpx.AsyncClient(timeout=120) as client:
            for address in self.remote_agent_addresses:
                card_resolver = A2ACardResolver(client, address)
                try:
                    card = await card_resolver.get_agent_card()
                    remote_connection = RemoteAgentConnections(
                        agent_card=card, agent_url=address
                    )
                    self.remote_agent_connections[card.name] = remote_connection
                    self.cards[card.name] = card
                except httpx.ConnectError as e:
                    LOGGER.warning(f"ERROR: Failed to get agent card from {address}: {e}")
                except Exception as e:
                    LOGGER.warning(f"ERROR: Failed to initialize connection for {address}: {e}")

            agent_info = [
                json.dumps({"name": card.name, "description": card.description})
                for card in self.cards.values()
            ]

        self.agents = "\n".join(agent_info) if agent_info else "No friends found"
        if not agent_info:
            LOGGER.info("No remote agents are online")
        else:
            LOGGER.info("remote agent info:", self.agents)

    async def get_root_agent(self):
        # we initialize the root agent with friends' status
        await self.check_remote_agent_connections()
        return self._agent


def _get_initialized_host_agent_sync():
    """Synchronously creates and initializes the HostAgent."""

    # Hardcoded URLs for the friend agents
    friend_agent_urls = [
        "http://localhost:8001",  # Alice's Agent
        "http://localhost:8002",  # Ben's Agent
        "http://localhost:8003",  # Charlie's Agent
    ]

    async def _async_main():
        LOGGER.info('Initializing host agent')
        hosting_agent_instance = HostAgent(
            remote_agent_addresses=friend_agent_urls
        )
        root_agent = await hosting_agent_instance.get_root_agent()
        LOGGER.info('HostAgent initialized')
        return root_agent

    return asyncio.run(_async_main())


root_agent = _get_initialized_host_agent_sync()

# Currently, the ADK documentation for ADK WEB demonstrates a sync initialization approach (for root agent).
# The ADK WEB only works via async methods, while the agents export a synchronous root_model.
# This creates an inconsistency that forces developers to implement workarounds
# to bridge async initialization with the synchronous export required by the ADK agent framework.

# nest_asyncio.apply() -- To resolve this, you can modify the async function to use the current running event loop instead of trying to start a new one.
