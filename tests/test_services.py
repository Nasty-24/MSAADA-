import sys
from pathlib import Path

# Add the MSAADA project root to Python's import path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from msaada.tools.service_search import search_government_services


def test_business_registration_found():
    result = search_government_services("business registration")

    assert "Business Registration" in result
    assert "Business Registration Service" in result


def test_unknown_service():
    result = search_government_services("something completely unknown")

    assert "No matching government service" in result


def test_business_keyword():
    result = search_government_services("business")

    assert "Business Registration" in result