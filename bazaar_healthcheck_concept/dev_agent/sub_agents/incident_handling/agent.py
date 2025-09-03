import uuid

from google.adk.agents import Agent


def create_incident_ticket(issue: str) -> dict:
    """Creates an incident ticket about an issue"""
    result = {
        "status": "incident ticket created",
        "ticket_number": str(uuid.uuid4()),
        "issue": issue,
    }
    print(f"--- Tool: create_incident_ticket called ---\n", result)

    return result


incident_handling_agent = Agent(
    name="incident_handling_agent",
    model="gemini-2.0-flash",
    description="An agent which handling incidents when a component has issues",
    instruction="""
    You are an incident handling agent in the Bazaar project.
    
    When a project component has issues, your tasks are:
    - create an incident ticket
    """,
    tools=[create_incident_ticket],
)
