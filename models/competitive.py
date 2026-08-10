from pydantic import BaseModel, Field


class CompetitiveFinding(BaseModel):
    competitor: str = Field(
        description="Name of the competitor."
    )

    threat_level: str = Field(
        description="Competitive threat level: low, medium, or high."
    )

    summary: str = Field(
        description="Summary of the competitive position."
    )

    impact: str = Field(
        description="How the competitive position affects the acquisition."
    )

    evidence_ids: list[str] = Field(
        default_factory=list
    )