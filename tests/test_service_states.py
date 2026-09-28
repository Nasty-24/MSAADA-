import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from msaada.tools.service_validation import validate_service
from msaada.tools.service_search import search_government_services


def test_business_registration_is_verified():
    result = validate_service("business_registration")

    assert '"validation_status": "VERIFIED"' in result
    assert '"verified": true' in result


def test_passport_is_unverified():
    result = validate_service("passport_application")

    assert '"validation_status": "VERIFIED"' in result
    assert '"verified": false' in result


def test_national_id_is_unverified():
    result = validate_service("national_id")

    assert '"validation_status": "UNVERIFIED"' in result
    assert '"verified": false' in result


def test_passport_requirements_are_not_claimed():
    result = search_government_services("passport")

    assert "passport_application" in result
assert "Duly filled application Form 19" in result


def test_national_id_requirements_are_not_claimed():
    result = search_government_services("national ID")

    assert '"requirements": []' in result