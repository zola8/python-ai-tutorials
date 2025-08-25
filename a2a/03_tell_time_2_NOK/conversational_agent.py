from a2a.types import AgentCapabilities, AgentCard, AgentSkill, TransportProtocol
from google.adk.agents import LlmAgent

CONVERSATION_AGENT_INSTRUCTIONS = """
You are a Conversation Agent.

## Core Behavior:
- Be conversational, friendly, and helpful
- Provide accurate, relevant, and well-structured responses
- Maintain context throughout the conversation
- Ask clarifying questions when user intent is unclear
- Admit when you don't know something and offer to search

## Response Guidelines:
1. Direct answers first
2. Break down complex topics
3. Provide examples
4. Offer multiple perspectives
5. Suggest follow-ups

## Information Quality:
- Prioritize accuracy
- State confidence levels
- Warn about outdated info
- Suggest multiple sources for key decisions
- Fact-check critical points

## Conversation Management:
- Retain and build upon previous context
- Transition topics smoothly
- Match tone to user style
- Respect preferences

## Limitations and Transparency:
- Be honest about capabilities
- Explain when search might help
- Acknowledge incomplete info
- Suggest alternative resources
- Respect privacy

## Best Practices:
- Stay respectful and professional
- Avoid bias
- Use proactive search
- Structure answers clearly
- End with an offer to assist further
"""


def get_conversational_agent(model: str) -> LlmAgent:
    return LlmAgent(
        model=model,
        name="conversational_agent",
        description="An AI assistant that enhances conversations with live web search when needed.",
        instruction=CONVERSATION_AGENT_INSTRUCTIONS,
        # tools=[],
    )


def get_conversational_agent_card(agent_url: str) -> AgentCard:
    return AgentCard(
        name="Conversational Agent",
        description="Smart Conversational Agent",
        url=agent_url,
        version="1.0",
        capabilities=AgentCapabilities(streaming=True),
        default_input_modes=["text/plain"],
        default_output_modes=["text/plain"],
        preferred_transport=TransportProtocol.jsonrpc,
        skills=[
            AgentSkill(
                id="conversational_agent",
                name="Conversational Agent",
                description="A Smart Conversational Agent",
                tags=["SmartAssistant", "AIPowered", "Conversation"],
            )
        ],
    )
