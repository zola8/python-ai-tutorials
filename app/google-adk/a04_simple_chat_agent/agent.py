from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

root_agent = LlmAgent(
    model=LiteLlm(model="ollama_chat/gemma3:latest"),
    name="a04_simple_chat_agent",
    description="You are helpful assistant.",
    instruction="Answer the users questions responding as a scottish pirate."
)

# the root_agent's name should be the same = as folder name
# https://www.youtube.com/watch?v=P4VFL9nIaIA
