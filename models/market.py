from pydantic import BaseModel, Field


class MarketFinding(BaseModel):
    topic: str = Field(
        description="The market or news topic being analyzed."
    )

    summary: str = Field(
        description="Summary of the relevant market or news development."
    )

    impact: str = Field(
        description="Potential impact on the acquisition."
    )

    sentiment: str = Field(
        description="Overall sentiment: positive, negative, or neutral."
    )

    evidence_ids: list[str] = Field(
        default_factory=list,
        description="Identifiers of supporting evidence."
    )