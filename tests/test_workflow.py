from msaada.tools.service_search import search_government_services
from msaada.tools.service_validation import validate_service


def test_business_service_is_verified():
    result = search_government_services("business registration")

    assert '"verified": true' in result
    assert '"status": "active"' in result

def test_business_service_has_validation_fields():
    result = search_government_services("business registration")

    assert '"requirements"' in result
    assert '"steps"' in result
    assert '"fees"' in result
    assert '"official_url"' in result
    assert '"last_verified"' in result


def test_business_service_validation():
    result = validate_service("business_registration")

    assert '"validation_status": "VERIFIED"' in result
    assert '"verified": true' in result
    assert '"requirements_available": true' in result
    assert '"steps_available": true' in result
    assert '"official_source_available": true' in result

def test_unknown_service_validation():
    result = validate_service("does_not_exist")

    assert '"validation_status": "NOT_FOUND"' in result