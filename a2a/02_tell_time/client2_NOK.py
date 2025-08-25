# TODO new (not deprecated) approach:
# https://deeplearningdispatch.com/2025/08/16/running-multiple-a2a-agents-on-a-single-server/

import asyncio
import uuid
from uuid import uuid4

import httpx
from a2a.client import A2ACardResolver, ClientConfig, ClientFactory
from a2a.types import TransportProtocol, Message, Role, Part, TextPart


async def main() -> str:
    base_url = 'http://localhost:8080'
    async with httpx.AsyncClient() as httpx_client:
        # Initialize A2ACardResolver
        resolver = A2ACardResolver(
            httpx_client=httpx_client,
            base_url=base_url,
        )

        public_card = (
            await resolver.get_agent_card()
        )
        json = public_card.model_dump_json(indent=2, exclude_none=True)
        print(f"Public card read on {base_url}/.well-known/agent-card.json \n", json)

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
        client = factory.create(public_card)
        print("A2AClient initialized.")

        context_id = str(uuid.uuid4())

        message_obj = Message(
            role=Role.user,
            parts=[Part(TextPart(text="What is the current time?"))],
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
                print(task.artifacts[0].parts[0].root.text)
                return task.artifacts[0].parts[0].root.text
            except (AttributeError, IndexError):
                return str(task)

        return "No response received"


if __name__ == '__main__':
    asyncio.run(main())
