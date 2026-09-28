import json
from pathlib import Path


def validate_service(service_id: str) -> str:
    """
    Validate a government service against the MSAADA knowledge base.
    """

    data_path = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "services.json"
    )

    try:
        with open(data_path, "r", encoding="utf-8") as file:
            services = json.load(file)

    except FileNotFoundError:
        return json.dumps({
            "validation_status": "ERROR",
            "message": "Government service database not found."
        }, indent=2)

    except json.JSONDecodeError:
        return json.dumps({
            "validation_status": "ERROR",
            "message": "Government service database contains invalid JSON."
        }, indent=2)

    service = services.get(service_id)

    if service is None:
        return json.dumps({
            "service_id": service_id,
            "validation_status": "NOT_FOUND",
            "message": (
                "The service does not exist in the "
                "MSAADA knowledge base."
            )
        }, indent=2)

    verified = service.get("verified", False)
    status = service.get("status", "unknown")

    requirements = service.get("requirements", [])
    steps = service.get("steps", [])
    official_url = service.get("official_url")
    source_name = service.get("source_name")
    source_type = service.get("source_type")

    requirements_available = bool(requirements)
    steps_available = bool(steps)
    official_source_available = bool(official_url)
    provenance_available = bool(
        service.get("source_provenance")
    )

    if (
        verified
        and status == "active"
        and requirements_available
        and steps_available
        and official_source_available
        and provenance_available
    ):
        validation_status = "VERIFIED"

    elif not verified:
        validation_status = "UNVERIFIED"

    else:
        validation_status = "INCOMPLETE"

    return json.dumps({
        "service_id": service_id,
        "service_name": service.get("name"),
        "agency": service.get("agency"),
        "validation_status": validation_status,
        "verified": verified,
        "status": status,
        "requirements_available": requirements_available,
        "steps_available": steps_available,
        "official_source_available": official_source_available,
        "source_name": source_name,
        "source_type": source_type,
        "last_verified": service.get("last_verified"),
        "message": (
            "Service passed MSAADA verification checks."
            if validation_status == "VERIFIED"
            else
            "Service information requires additional verification."
        )
    }, indent=2)