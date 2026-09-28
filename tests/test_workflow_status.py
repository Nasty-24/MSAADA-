import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from msaada.tools.workflow_status import create_workflow_status


def test_verified_service_is_ready_for_action():
    result = create_workflow_status(
        "business_registration",
        "VERIFIED",
        True,
        True,
    )

    assert '"outcome": "READY_FOR_ACTION"' in result


def test_unverified_service_requires_verification():
    result = create_workflow_status(
        "business_registration",
        "UNVERIFIED",
        False,
        False,
    )

    assert '"outcome": "REQUIRES_VERIFICATION"' in result


def test_incomplete_service_is_flagged():
    result = create_workflow_status(
        "business_registration",
        "INCOMPLETE",
        True,
        False,
    )

    assert '"outcome": "INFORMATION_INCOMPLETE"' in result