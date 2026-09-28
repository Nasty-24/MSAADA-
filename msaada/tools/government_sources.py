from dataclasses import dataclass
from typing import Optional


@dataclass
class GovernmentSource:
    name: str
    agency: str
    url: str
    source_type: str
    api_available: bool = False
    api_url: Optional[str] = None


GOVERNMENT_SOURCES = {
    "immigration": GovernmentSource(
        name="Directorate of Immigration Services",
        agency="Directorate of Immigration Services",
        url="https://immigration.go.ke/",
        source_type="official_government_website",
    ),

    "ecitizen": GovernmentSource(
        name="eCitizen",
        agency="Government of Kenya",
        url="https://www.ecitizen.go.ke/",
        source_type="official_government_platform",
    ),

    "kra": GovernmentSource(
        name="Kenya Revenue Authority",
        agency="Kenya Revenue Authority",
        url="https://www.kra.go.ke/",
        source_type="official_government_website",
    ),

    "ntsa": GovernmentSource(
        name="National Transport and Safety Authority",
        agency="National Transport and Safety Authority",
        url="https://www.ntsa.go.ke/",
        source_type="official_government_website",
    ),

    "huduma": GovernmentSource(
        name="Huduma Kenya",
        agency="Huduma Kenya",
        url="https://www.hudumakenya.go.ke/",
        source_type="official_government_platform",
    ),
}


def get_government_source(source_id: str) -> Optional[GovernmentSource]:
    """
    Return an official government source by ID.
    """

    return GOVERNMENT_SOURCES.get(source_id)


def list_government_sources() -> list[dict]:
    """
    Return registered government sources.
    """

    return [
        {
            "id": source_id,
            "name": source.name,
            "agency": source.agency,
            "url": source.url,
            "source_type": source.source_type,
            "api_available": source.api_available,
            "api_url": source.api_url,
        }
        for source_id, source in GOVERNMENT_SOURCES.items()
    ]