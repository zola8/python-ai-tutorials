from langgraph_supervisor import create_supervisor

from a01_file_agent import file_manager_agent
from a01_main import llm, print_stream
from a01_math_agent import math_agent

supervisor = create_supervisor(
    model=llm,
    agents=[file_manager_agent, math_agent],
    prompt=(
        "You are a supervisor managing two agents:\n"
        "- a file manager agent. Assign file and folder related tasks to this agent\n"
        "- a math agent. Assign math-related tasks to this agent\n"
        "Assign work to one agent at a time, do not call agents in parallel.\n"
        "Do not do any work yourself."
    ),
    add_handoff_back_messages=True,
    output_mode="full_history",
).compile()

if __name__ == "__main__":
    messages = {"messages": [{"role": "user", "content": "How much 7 * (1 + 2)"}]}
    # messages = {"messages": [{"role": "user", "content": "List files from this folder: C:/DEV"}]}
    print_stream(supervisor.stream(messages, stream_mode="values", debug=False))

    # NOK
    # https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/multi_agent/agent_supervisor.md
