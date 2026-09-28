import sys
from pathlib import Path

# Add the MSAADA project root to Python's import path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from msaada.tools.service_validation import validate_service


def test_business_service_is_verified():
    result = validate_service("business_registration")

    assert '"validation_status": "VERIFIED"' in result
    assert '"verified": true' in result
    
def test_unknown_service_is_not_found():
    result = validate_service("fake_government_service")

    assert '"validation_status": "NOT_FOUND"' in result