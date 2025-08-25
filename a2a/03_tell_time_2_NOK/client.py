import asyncio
import uuid
from typing import Any
from uuid import uuid4

import httpx
from a2a.client import ClientConfig, ClientFactory
from a2a.types import AgentCard, Message, Part, Role, TextPart, TransportProtocol

AGENT_CARD_PATH = "/agent-card.json"


class A2AClient:
    def __init__(self, default_timeout: float = 240.0):
        # Cache for agent metadata
        self._agent_info_cache: dict[str, dict[str, Any] | None] = {}
        self.default_timeout = default_timeout

    async def create_task(self, agent_url: str, message: str, context_id: str) -> str:
        """Send a message following the official A2A SDK pattern."""
        # Configure httpx client with timeout
        timeout_config = httpx.Timeout(
            timeout=self.default_timeout,
            connect=10.0,
            read=self.default_timeout,
            write=10.0,
            pool=5.0,
        )

        async with httpx.AsyncClient(timeout=timeout_config) as httpx_client:
            # Check if we have cached agent card data
            if agent_url in self._agent_info_cache and self._agent_info_cache[agent_url] is not None:
                agent_card_data = self._agent_info_cache[agent_url]
            else:
                # Fetch the agent card
                agent_card_response = await httpx_client.get(f"{agent_url}{AGENT_CARD_PATH}")
                agent_card_data = self._agent_info_cache[agent_url] = agent_card_response.json()

            # Create AgentCard from data
            agent_card = AgentCard(**agent_card_data)

            # Create A2A client with the agent card
            config = ClientConfig(
                httpx_client=httpx_client,
                supported_transports=[
                    TransportProtocol.jsonrpc,
                    TransportProtocol.http_json,
                ],
                use_client_preference=True,
            )

            factory = ClientFactory(config)
            client = factory.create(agent_card)
            message_obj = Message(
                role=Role.user,
                parts=[Part(TextPart(text=message))],
                message_id=str(uuid4()),
                context_id=context_id,
            )
            responses = []
            async for response in client.send_message(message_obj):
                responses.append(response)
            # The response is a tuple - get the first element (Task object)
            if responses and isinstance(responses[0], tuple) and len(responses[0]) > 0:
                task = responses[0][0]  # First element of the tuple

                # Extract text: task.artifacts[0].parts[0].root.text
                try:
                    return task.artifacts[0].parts[0].root.text
                except (AttributeError, IndexError):
                    return str(task)

            return "No response received"


async def main():
    a2a_client: A2AClient = A2AClient()
    agent_host_url = "http://localhost:8080/a2a"

    context_id = str(uuid.uuid4())
    print(f"Starting conversation with context_id: {context_id}")

    # Turn 1 — Start conversation
    conversation_task = await a2a_client.create_task(
        agent_url=f"{agent_host_url}/conversation",
        message="Where is Zürich?",
        context_id=context_id,
    )
    print(f"Turn 1 → {conversation_task} \n\n")

    # Turn 2 — Follow-up using pronoun (tests context memory)
    conversation_task = await a2a_client.create_task(
        agent_url=f"{agent_host_url}/conversation",
        message="What city am I looking for?",
        context_id=context_id,
    )
    print(f"Turn 2 → {conversation_task} \n\n")

    # Turn 3 — A context shift
    conversation_task = await a2a_client.create_task(
        agent_url=f"{agent_host_url}/telltime",
        message="What is the time?",
        context_id=context_id,
    )
    print(f"Turn 4 → {conversation_task}")


if __name__ == '__main__':
    asyncio.run(main())
