from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from pydantic import BaseModel, Field


# --- Define Output Schema ---
class EmailContent(BaseModel):
    subject: str = Field(
        description="The subject line of the email. Should be concise and descriptive."
    )
    body: str = Field(
        description="The main content of the email. Should be well-formatted with proper greeting, paragraphs, and signature."
    )


# --- Create Email Generator Agent ---
root_agent = LlmAgent(
    name="a05_structured_output",
    model=LiteLlm(model="ollama_chat/gemma3:latest"),
    instruction="""
        You are an Email Generation Assistant.
        Your task is to generate a professional email based on the user's request.

        GUIDELINES:
        - Create an appropriate subject line (concise and relevant)
        - Write a well-structured email body with:
            * Professional greeting
            * Clear and concise main content
            * Appropriate closing
            * Your name as signature
        - Suggest relevant attachments if applicable (empty list if none needed)
        - Email tone should match the purpose (formal for business, friendly for colleagues)
        - Keep emails concise but complete

        IMPORTANT: Your response MUST be valid JSON matching this structure:
        {
            "subject": "Subject line here",
            "body": "Email body here with proper paragraphs and formatting",
        }

        DO NOT include any explanations or additional text outside the JSON response.
    """,
    description="Generates professional emails with structured subject and body",
    output_schema=EmailContent,
    output_key="email",
)

# https://github.com/bhancockio/agent-development-kit-crash-course/tree/main/4-structured-outputs
# https://www.youtube.com/watch?v=P4VFL9nIaIA

# When using output_schema:
#
# No Tool Usage: Agents with an output schema cannot use tools during their execution
# Direct JSON Response: The LLM must produce a JSON response matching the schema as its final output
# Clear Instructions: The agent's instructions must explicitly guide the LLM to produce properly formatted JSON
