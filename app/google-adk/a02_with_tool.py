import asyncio
import os
from datetime import datetime

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

os.environ["OLLAMA_API_BASE"] = "http://localhost:11434"

# Define constants for identifying the interaction context
APP_NAME = "tutorial_app"
USER_ID = "user_1"
SESSION_ID = "session_001"  # Using a fixed ID for simplicity


def get_current_time() -> dict:
    """Returns the current time."""
    now = datetime.now()
    report = (
        f'The current time is {now.strftime("%Y-%m-%d %H:%M:%S")}'
    )
    return {"status": "success", "report": report}


root_agent = LlmAgent(
    name="time_agent",
    model=LiteLlm(model="ollama_chat/llama3.2:latest"),
    description=(
        "Agent to answer questions about the time."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time."
    ),
    tools=[get_current_time],
)


async def call_agent_async(query: str, runner, user_id, session_id):
    """Sends a query to the agent and prints the final response."""
    print(f"\n>>> User Query: {query}")

    # Prepare the user's message in ADK format
    content = types.Content(role='user', parts=[types.Part(text=query)])

    final_response_text = "Agent did not produce a final response."  # Default

    # Key Concept: run_async executes the agent logic and yields Events.
    # We iterate through events to find the final answer.
    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
        # You can uncomment the line below to see *all* events during execution
        # print(f"  [Event] Author: {event.author}, Type: {type(event).__name__}, Final: {event.is_final_response()}, Content: {event.content}")

        # Key Concept: is_final_response() marks the concluding message for the turn.
        if event.is_final_response():
            if event.content and event.content.parts:
                # Assuming text response in the first part
                final_response_text = event.content.parts[0].text
            elif event.actions and event.actions.escalate:  # Handle potential errors/escalations
                final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
            # Add more checks here if needed (e.g., specific error codes)
            break  # Stop processing events once the final response is found

    print(f"<<< Agent Response: {final_response_text}")


async def main() -> None:
    # InMemorySessionService is simple, non-persistent storage for this tutorial.
    session_service = InMemorySessionService()

    # Create the specific session where the conversation will happen
    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    print(f"Session created: App='{APP_NAME}', User='{USER_ID}', Session='{session.id}'")

    # --- Runner ---
    # Key Concept: Runner orchestrates the agent execution loop.
    runner = Runner(
        agent=root_agent,  # The agent we want to run
        app_name=APP_NAME,  # Associates runs with our app
        session_service=session_service  # Uses our session manager
    )
    print(f"Runner created for agent '{runner.agent.name}'.")

    await call_agent_async("what is the time?",
                           runner=runner,
                           user_id=USER_ID,
                           session_id=SESSION_ID)


if __name__ == "__main__":
    asyncio.run(main())
