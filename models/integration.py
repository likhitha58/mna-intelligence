from pydantic import BaseModel, Field


class IntegrationFinding(BaseModel):
    integration_area: str = Field(
        description="The area of integration being analyzed."
    )

    timeline: str = Field(
        description="Estimated high-level timeline for integration."
    )

    difficulty: str = Field(
        description="Integration difficulty level: Low, Medium, or High."
    )

    summary: str = Field(
        description="Summary of the proposed integration approach."
    )

    key_actions: list[str] = Field(
        description="Important actions required for successful integration."
    )

    evidence_ids: list[str] = Field(
        default_factory=list
    )