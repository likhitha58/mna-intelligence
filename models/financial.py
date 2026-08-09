from pydantic import BaseModel, Field


class FinancialFinding(BaseModel):
    metric: str = Field(
        description="The financial metric being analyzed."
    )

    value: str = Field(
        description="The reported value of the metric."
    )

    period: str = Field(
        description="Financial period associated with the metric."
    )

    interpretation: str = Field(
        description="Interpretation of the metric in the context of the acquisition."
    )

    evidence_ids: list[str] = Field(
        default_factory=list,
        description="Identifiers of supporting evidence."
    )