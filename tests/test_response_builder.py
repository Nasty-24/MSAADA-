import sys
from pathlib import Path
import json

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from msaada.tools.response_builder import build_citizen_response


def test_verified_service_produces_actionable_response():

    service = {
        "name": "Business Registration",
        "agency": "Business Registration Service (BRS)",
        "requirements": [
            "eCitizen account",
            "National ID"
        ],
        "steps": [
            "Sign in to eCitizen.",
            "Open Business Registration Service."
        ],
        "official_url": "https://brs.go.ke/"
    }

    validation = {
        "validation_status": "VERIFIED"
    }

    result = build_citizen_response(service, validation)

    assert "Business Registration" in result
    assert "VERIFIED" in result
    assert "National ID" in result
    assert "eCitizen" in result
    assert "https://brs.go.ke/" in result


def test_unverified_service_does_not_invent_requirements():

    service = {
        "name": "Kenyan Passport Application",
        "agency": "Directorate of Immigration Services",
        "requirements": []
    }

    validation = {
        "validation_status": "UNVERIFIED"
    }

    result = build_citizen_response(service, validation)

    assert "UNVERIFIED" in result
    assert "UNVERIFIED" in result
    assert "requirements, fees or procedures as confirmed facts" in result
    assert "I will not present unverified information as fact" in result


def test_incomplete_service_is_flagged():

    service = {
        "name": "Example Service",
        "agency": "Example Agency"
    }

    validation = {
        "validation_status": "INCOMPLETE"
    }

    result = build_citizen_response(service, validation)

    assert "INCOMPLETE" in result
    assert "missing" in result