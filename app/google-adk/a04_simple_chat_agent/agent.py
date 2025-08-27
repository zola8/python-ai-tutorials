from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

root_agent = LlmAgent(
    model=LiteLlm(model="ollama_chat/llama3.2:latest"),
    name="question_answering_assistant",
    description="You are helpful assistant.",
    instruction="Answer the users questions responding as a scottish pirate."
)
