import uvicorn
from a2a.server.apps import A2AFastAPIApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCard, AgentSkill, AgentCapabilities

from tell_time_agent import TellTimeAgentExecutor

agent_host_url = "http://localhost:8080"

skill = AgentSkill(
    id='id_tell_time',
    name='Returns the current time',
    description='Tells the current time when asked',
    tags=['tell time'],
)

public_agent_card = AgentCard(
    name='TellTime Agent',
    description='Tells the current time agent',
    url=agent_host_url,
    version='1.0.0',
    default_input_modes=['text'],
    default_output_modes=['text'],
    capabilities=AgentCapabilities(streaming=False),
    skills=[skill],  # Only the basic skill for the public card
    supports_authenticated_extended_card=False,
)

request_handler = DefaultRequestHandler(
    agent_executor=TellTimeAgentExecutor(),
    task_store=InMemoryTaskStore(),
)

server = A2AFastAPIApplication(
    agent_card=public_agent_card,
    http_handler=request_handler,
)

if __name__ == "__main__":
    uvicorn.run(server.build(), host='0.0.0.0', port=8080)

# http://localhost:8080/
# http://localhost:8080/.well-known/agent-card.json

