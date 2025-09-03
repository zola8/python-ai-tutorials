import random

from pydantic import BaseModel, Field


# --- Define Output Schema ---
class HealthcheckContent(BaseModel):
    environment: str = Field(
        description="Environment where the issue happened. Can be DEV, PROD."
    )
    component: str = Field(
        description="Component where the issue was detected. Can be frontend, backend."
    )
    text: str = Field(
        description="The description of the issue. Can be 'OK' when there is no issue."
    )
    severity: str = Field(
        description="The severity category of the issue. Can be low, medium or high. Empty when there is no issue."
    )


def healthcheck_backend(environment: str) -> HealthcheckContent:
    """
    Checking the health status of the backend on a specified environment.
    """
    rand = random.randint(1, 5)

    if rand == 1:
        return HealthcheckContent(environment=environment, component="backend",
                                  text="Sonar warning found: deprecated method is used", severity="low")
    elif rand == 2:
        return HealthcheckContent(environment=environment, component="backend",
                                  text="Build failed due to unit test", severity="high")
    else:
        return HealthcheckContent(environment=environment, component="backend", text="OK", severity="")


def healthcheck_frontend(environment: str) -> HealthcheckContent:
    """
    Checking the health status of the frontend on a specified environment.
    """
    rand = random.randint(1, 5)

    if rand == 1:
        return HealthcheckContent(environment=environment, component="frontend",
                                  text="Property font is deprecated and will be removed in the future release",
                                  severity="low")
    elif rand == 2:
        return HealthcheckContent(environment=environment, component="frontend", text="Internal Server Error",
                                  severity="high")
    else:
        return HealthcheckContent(environment=environment, component="frontend", text="OK", severity="")
