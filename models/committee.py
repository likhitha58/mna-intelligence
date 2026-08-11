from pydantic import BaseModel, Field


class CommitteeDecision(BaseModel):
    recommendation: str = Field(
        description=(
            "Overall acquisition recommendation. "
            "Examples: Proceed, Proceed with Caution, or Do Not Proceed."
        )
    )

    strategic_rationale: str = Field(
        description="Overall strategic reasoning behind the recommendation."
    )

    financial_assessment: str = Field(
        description="Assessment of the financial attractiveness and limitations."
    )

    key_opportunities: list[str] = Field(
        description="Most important opportunities created by the acquisition."
    )

    key_risks: list[str] = Field(
        description="Most important risks that could affect the acquisition."
    )

    regulatory_concerns: list[str] = Field(
        description="Major regulatory concerns identified across the analysis."
    )

    integration_concerns: list[str] = Field(
        description="Major technology, organizational, and integration concerns."
    )

    valuation_assessment: str = Field(
        description="Assessment of the valuation and the reliability of its assumptions."
    )

    conditions_before_acquisition: list[str] = Field(
        description="Important conditions that should be satisfied before proceeding."
    )

    confidence: str = Field(
        description="Confidence level in the overall recommendation."
    )