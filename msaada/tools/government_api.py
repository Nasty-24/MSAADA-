import os
from typing import Any

import requests


GAVACONNECT_BASE_URL = os.getenv(
    "GAVACONNECT_BASE_URL",
    ""
)

GAVACONNECT_API_KEY = os.getenv(
    "GAVACONNECT_API_KEY",
    ""
)


def gavaconnect_available() -> bool:
    """
    Check whether GavaConnect credentials have been configured.
    """

    return bool(
        GAVACONNECT_BASE_URL and
        GAVACONNECT_API_KEY
    )


def call_gavaconnect(
    endpoint: str,
    params: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """
    Generic GavaConnect API adapter.

    This intentionally does not assume a specific government API
    endpoint until the corresponding API has been provisioned and
    documented for the project.
    """

    if not gavaconnect_available():
        return {
            "success": False,
            "source": "gavaconnect",
            "status": "not_configured",
            "message": (
                "GavaConnect credentials or base URL have not "
                "been configured."
            ),
        }

    url = f"{GAVACONNECT_BASE_URL.rstrip('/')}/{endpoint.lstrip('/')}"

    headers = {
        "Authorization": f"Bearer {GAVACONNECT_API_KEY}",
        "Accept": "application/json",
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params or {},
            timeout=10,
        )

        response.raise_for_status()

        return {
            "success": True,
            "source": "gavaconnect",
            "status": "ok",
            "data": response.json(),
        }

    except requests.RequestException as exc:
        return {
            "success": False,
            "source": "gavaconnect",
            "status": "error",
            "message": str(exc),
        }