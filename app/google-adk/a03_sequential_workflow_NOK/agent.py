from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.models.lite_llm import LiteLlm

agent_A = LlmAgent(
    name="AgentA",
    model=LiteLlm(model="ollama_chat/gemma3:latest"),
    instruction="Find the capital of France.",
    output_key="capital_city"
)
agent_B = LlmAgent(
    name="AgentB",
    model=LiteLlm(model="ollama_chat/gemma3:latest"),
    instruction="Tell me about the city stored in {capital_city}."
)

pipeline = SequentialAgent(
    name="a03_sequential_workflow_NOK",
    sub_agents=[agent_A, agent_B],
)
