# https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/multi_agent/agent_supervisor.md
import os

from langgraph.prebuilt import create_react_agent

from a01_main import llm, print_stream


def list_files(directory: str = ".") -> list:
    """List all files in a directory."""
    return os.listdir(directory)


def read_file(filepath: str) -> str:
    """Read and return the contents of a file."""
    with open(filepath, 'r') as f:
        return f.read()


file_manager_agent = create_react_agent(
    model=llm,
    tools=[list_files, read_file],
    prompt=(
        "You are a file manager agent.\n\n"
        "INSTRUCTIONS:\n"
        "- Assist ONLY with file search and file read tasks, DO NOT do any math\n"
        "- After you're done with your tasks, respond to the supervisor directly\n"
        "- Respond ONLY with the results of your work, do NOT include ANY other text."
    ),
    name="file_manager_agent",
)

if __name__ == "__main__":
    messages = {"messages": [
        {"role": "user", "content": "what files are in C:/DEV"},
        # {"role": "user", "content": "can you read this file: C:/DEV/test.txt "},
    ]}
    print_stream(file_manager_agent.stream(messages, stream_mode="values"))
