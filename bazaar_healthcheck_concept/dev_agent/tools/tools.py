import random


def healthcheck_backend() -> dict:
    """
    Checking the health status of the backend.
    """
    rand = random.randint(1, 5)

    if rand == 1:
        status = {
            "text": "Sonar warning found: deprecated method is used",
            "severity": "low"
        }
    elif rand == 2:
        status = {
            "text": "Build failed due to unit test",
            "severity": "high"
        }
    else:
        status = {
            "text": "OK",
            "severity": ""
        }

    return {
        "status_backend": status,
    }


def healthcheck_frontend() -> dict:
    """
    Checking the health status of the frontend.
    """
    rand = random.randint(1, 5)

    if rand == 1:
        status = {
            "text": "Property font is deprecated and will be removed in the future release",
            "severity": "low"
        }
    elif rand == 2:
        status = {
            "text": "Internal Server Error",
            "severity": "high"
        }
    else:
        status = {
            "text": "OK",
            "severity": ""
        }

    return {
        "status_frontend": status,
    }
