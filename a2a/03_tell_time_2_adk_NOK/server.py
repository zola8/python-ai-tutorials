import logging

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from conversational_agent import get_conversational_agent, get_conversational_agent_card
from tell_time_agent import get_telltime_agent, get_telltime_agent_card
from utils import A2AUtils

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

AGENT_BASE_URL = "localhost:8080"
MODEL_NAME = "ollama_chat/llama3.2"

app: FastAPI = FastAPI(
    title="Run multiple agents on single host using A2A protocol.",
    description="Run multiple agents on single host using A2A protocol.",
    version="1.0.0",
    root_path="/a2a",
)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


# conversation agent integration with A2A server
A2AUtils.build(
    name="conversation",
    get_agent=get_conversational_agent,
    get_agent_card=get_conversational_agent_card,
    model_name=MODEL_NAME,
    agent_base_url=AGENT_BASE_URL,
    app=app,
)

# trending_topics agent integration with A2A server
A2AUtils.build(
    name="telltime",
    get_agent=get_telltime_agent,
    get_agent_card=get_telltime_agent_card,
    model_name=MODEL_NAME,
    agent_base_url=AGENT_BASE_URL,
    app=app,
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

# https://deeplearningdispatch.com/2025/08/16/running-multiple-a2a-agents-on-a-single-server/
