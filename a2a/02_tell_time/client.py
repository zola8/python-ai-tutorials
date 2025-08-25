import asyncio
from typing import Any
from uuid import uuid4

import httpx
from a2a.client import A2ACardResolver, A2AClient
from a2a.types import SendMessageRequest, MessageSendParams

agent_host_url = "http://localhost:8080/"


async def main() -> None:
    async with httpx.AsyncClient() as httpx_client:
        # Initialize A2ACardResolver
        resolver = A2ACardResolver(
            httpx_client=httpx_client,
            base_url=agent_host_url,
        )

        public_card = (
            await resolver.get_agent_card()
        )
        json = public_card.model_dump_json(indent=2, exclude_none=True)
        print(f"Public card read on {agent_host_url}/.well-known/agent-card.json \n", json)

        # TODO this is deprecated now!
        client = A2AClient(
            httpx_client=httpx_client, agent_card=public_card
        )
        print("A2AClient initialized.")

        send_message_payload: dict[str, Any] = {
            'message': {
                'role': 'user',
                'parts': [
                    {'kind': 'text', 'text': 'What is the current time?'}
                ],
                'messageId': uuid4().hex,
            },
        }
        request = SendMessageRequest(
            id=str(uuid4()), params=MessageSendParams(**send_message_payload)
        )

        response = await client.send_message(request)
        response_json = response.model_dump(mode='json', exclude_none=True)
        result = response_json["result"]["parts"][0]["text"]
        print("result:", result)


if __name__ == '__main__':
    asyncio.run(main())
