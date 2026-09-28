import json
from pathlib import Path


def search_government_services(query: str) -> str:
    """
    Search the MSAADA government-service knowledge base.

    Searches across:
    - service ID
    - service name
    - agency
    - description
    - requirements
    - steps
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
            "error": "Government service database not found."
        })

    except json.JSONDecodeError:
        return json.dumps({
            "error": "Government service database contains invalid JSON."
        })

    if not query or not query.strip():
        return json.dumps({
            "error": "Please describe the government service you need."
        })

    query_words = query.lower().split()
    matches = []

    for service_id, service in services.items():

        searchable_parts = [
            service_id,
            service.get("name", ""),
            service.get("agency", ""),
            service.get("description", ""),
            service.get("source", ""),
            service.get("source_name", ""),
        ]

        searchable_parts.extend(
            service.get("requirements", [])
        )

        searchable_parts.extend(
            service.get("steps", [])
        )

        searchable_text = " ".join(
            str(part) for part in searchable_parts
        ).lower()

        score = 0

        for word in query_words:
            if word in searchable_text:
                score += 1

        if score > 0:
            matches.append(
                (score, service_id, service)
            )

    if not matches:
        return json.dumps({
            "found": False,
            "message": (
                "No matching government service was found. "
                "Please provide more details."
            )
        }, indent=2)

    matches.sort(
        reverse=True,
        key=lambda item: item[0]
    )

    results = []

    for score, service_id, service in matches:
        results.append({
            "id": service_id,
            "match_score": score,
            **service
        })

    return json.dumps({
        "found": True,
        "results": results
    }, indent=2)