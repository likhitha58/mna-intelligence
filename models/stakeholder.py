from pydantic import BaseModel, Field


class StakeholderFinding(BaseModel):
    stakeholder_group: str = Field(
        description="The stakeholder group affected by the acquisition."
    )

    impact_level: str = Field(
        description="Impact level: High, Medium, or Low."
    )

    impact_type: str = Field(
        description="Whether the impact is Positive, Negative, or Neutral."
    )

    summary: str = Field(
        description="Summary of the most important stakeholder impact."
    )

    implication: str = Field(
        description="Why this stakeholder impact matters to the acquisition."
    )

    evidence_ids: list[str] = Field(
        default_factory=list
    )