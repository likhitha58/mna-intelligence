from models.evidence import Evidence
from utils.evidence import generate_evidence_id


def create_evidence(
    source_name: str,
    source_type: str,
    content: str,
    relevance: str,
    url: str | None = None,
    title: str | None = None,
    published_at: str | None = None,
    credibility: str = "medium",
) -> Evidence:

    return Evidence(
        evidence_id=generate_evidence_id(),
        source_name=source_name,
        source_type=source_type,
        url=url,
        title=title,
        published_at=published_at,
        content=content,
        relevance=relevance,
        credibility=credibility,
    )