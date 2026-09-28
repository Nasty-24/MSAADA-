import json


def create_workflow_status(
    service_id: str,
    validation_status: str,
    requirements_available: bool,
    steps_available: bool,
) -> str:
    """
    Creates a structured MSAADA workflow status.
    """

    if validation_status == "VERIFIED":
        outcome = "READY_FOR_ACTION"

    elif validation_status == "UNVERIFIED":
        outcome = "REQUIRES_VERIFICATION"

    elif validation_status == "INCOMPLETE":
        outcome = "INFORMATION_INCOMPLETE"

    else:
        outcome = "SERVICE_NOT_FOUND"

    return json.dumps(
        {
            "service_id": service_id,
            "validation_status": validation_status,
            "requirements_available": requirements_available,
            "steps_available": steps_available,
            "outcome": outcome,
        },
        indent=2,
    )