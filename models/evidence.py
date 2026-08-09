from pydantic import BaseModel, Field


class Evidence(BaseModel):
    source_name: str = Field(
        description="Name of the source containing the evidence."
    )

    source_type: str = Field(
        description="Type of source, such as annual_report, filing, news, or market_data."
    )

    url: str | None = Field(
        default=None,
        description="URL of the source if available."
    )

    content: str = Field(
        description="The specific evidence extracted from the source."
    )

    relevance: str = Field(
        description="Why this evidence is relevant to the M&A analysis."
    )