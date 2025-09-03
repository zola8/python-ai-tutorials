import uuid

from google.adk.agents import Agent

from ...tools.tools import HealthcheckContent


def create_incident_ticket(healthcheck_status: HealthcheckContent) -> dict:
    """
    Creates an incident ticket about an issue.

    Args:
        healthcheck_status (HealthcheckContent): The status report from the healthcheck.
    """
    result = {
        "ticket_number": str(uuid.uuid4()),
        "issue": healthcheck_status,
    }
    print(f"---Incident ticket created ---\n", result)

    return result


incident_handling_agent = Agent(
    name="incident_handling_agent",
    model="gemini-2.0-flash",
    description="An agent which handling incidents when a component has issues",
    instruction="""
    You are an incident handling agent in a project.
    
    When a project component has issues, your tasks are:
    - create an incident ticket
    """,
    tools=[create_incident_ticket],
)
