import asyncio
import sys
import traceback

from beeai_framework.adapters.ollama import OllamaChatModel
from beeai_framework.agents.react import ReActAgent
from beeai_framework.errors import FrameworkError
from beeai_framework.memory import UnconstrainedMemory


async def main() -> None:
    agent = ReActAgent(
        llm=OllamaChatModel("llama3.2"),
        memory=UnconstrainedMemory(),
        tools=[],
    )

    # Matching events on the instance level
    agent.emitter.match("*.*", lambda data, event: None)

    # Matching events on the execution (run) level
    await agent.run("Hello agent!").observe(
        lambda emitter: emitter.match("*.*", lambda data, event: print(f"RUN LOG: received event '{event.path}'"))
    )


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except FrameworkError as e:
        traceback.print_exc()
        sys.exit(e.explain())



# RUN LOG: received event 'run.agent.react.start'
# RUN LOG: received event 'agent.react.start'
# RUN LOG: received event 'run.backend.ollama.chat.start'
# RUN LOG: received event 'backend.ollama.chat.start'
# RUN LOG: received event 'backend.ollama.chat.new_token'
# RUN LOG: received event 'backend.ollama.chat.new_token'
# RUN LOG: received event 'backend.ollama.chat.new_token'
# RUN LOG: received event 'backend.ollama.chat.new_token'
# RUN LOG: received event 'backend.ollama.chat.new_token'
# RUN LOG: received event 'backend.ollama.chat.new_token'
# RUN LOG: received event 'backend.ollama.chat.new_token'
# RUN LOG: received event 'backend.ollama.chat.new_token'
# RUN LOG: received event 'backend.ollama.chat.new_token'
# RUN LOG: received event 'backend.ollama.chat.new_token'
# RUN LOG: received event 'backend.ollama.chat.new_token'
# RUN LOG: received event 'backend.ollama.chat.new_token'
# RUN LOG: received event 'backend.ollama.chat.new_token'
# RUN LOG: received event 'backend.ollama.chat.success'
# RUN LOG: received event 'backend.ollama.chat.finish'
# RUN LOG: received event 'run.backend.ollama.chat.success'
# RUN LOG: received event 'run.backend.ollama.chat.finish'
# RUN LOG: received event 'agent.react.partial_update'
# RUN LOG: received event 'agent.react.update'
# RUN LOG: received event 'agent.react.partial_update'
# RUN LOG: received event 'agent.react.update'
# RUN LOG: received event 'agent.react.success'
# RUN LOG: received event 'run.agent.react.success'
# RUN LOG: received event 'run.agent.react.finish'
#
# Process finished with exit code 0
