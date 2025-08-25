from datetime import datetime

from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message


class TellTimeAgent:
    async def invoke(self) -> str:
        # Get the current system time as a formatted string.
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class TellTimeAgentExecutor(AgentExecutor):
    """AgentProxy Implementation."""

    def __init__(self):
        self.agent = TellTimeAgent()

    async def execute(
            self,
            context: RequestContext,
            event_queue: EventQueue,
    ) -> None:
        result = await self.agent.invoke()
        await event_queue.enqueue_event(new_agent_text_message(result))

    async def cancel(
            self, context: RequestContext, event_queue: EventQueue
    ) -> None:
        raise Exception('cancel not supported')
