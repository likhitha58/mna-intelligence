from pydantic import BaseModel, Field


class LegalFinding(BaseModel):
    issue: str = Field(
        description="The legal issue identified."
    )

    severity: str = Field(
        description="Severity of the legal issue: low, medium, or high."
    )

    summary: str = Field(
        description="Summary of the legal finding."
    )

    impact: str = Field(
        description="How the legal issue could affect the acquisition."
    )

    evidence_ids: list[str] = Field(
        default_factory=list
    )