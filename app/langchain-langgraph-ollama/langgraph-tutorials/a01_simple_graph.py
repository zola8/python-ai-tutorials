# https://github.com/techwithtim/LangGraph-Tutorial/blob/main/main.py
# https://www.youtube.com/watch?v=1w5cCXlh7JQ

from typing import Annotated

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

load_dotenv()

llm = init_chat_model(
    "ollama:llama3.2"
)


class State(TypedDict):
    messages: Annotated[list, add_messages]


def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}


graph_builder = StateGraph(State)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile()

if __name__ == "__main__":
    user_input = input("Enter a message: ")
    state = graph.invoke({"messages": [{"role": "user", "content": user_input}]})
    print(state["messages"][-1].content)
