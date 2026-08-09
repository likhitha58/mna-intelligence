from pydantic import BaseModel, Field


class Evidence(BaseModel):
    evidence_id: str = Field(
        description="Unique identifier for this evidence."
    )

    source_name: str = Field(
        description="Name of the source."
    )

    source_type: str = Field(
        description="Type of source, such as annual_report, filing, news, or market_data."
    )

    url: str | None = Field(
        default=None,
        description="URL of the source."
    )

    title: str | None = Field(
        default=None,
        description="Title of the source or document."
    )

    published_at: str | None = Field(
        default=None,
        description="Publication date or timestamp."
    )

    content: str = Field(
        description="Specific information extracted from the source."
    )

    relevance: str = Field(
        description="Why this evidence is relevant to the M&A analysis."
    )

    credibility: str = Field(
        description="Estimated credibility of the source: high, medium, or low."
    )