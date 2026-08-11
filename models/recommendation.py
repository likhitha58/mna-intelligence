from pydantic import BaseModel, Field


class FinalRecommendation(BaseModel):

    recommendation: str = Field(
        description=(
            "Overall acquisition recommendation. "
            "Use one of: Proceed, Proceed with Caution, or Do Not Proceed."
        )
    )

    strategic_rationale: str = Field(
        description="Main strategic reasons supporting the recommendation."
    )

    financial_assessment: str = Field(
        description="Assessment of the financial attractiveness of the acquisition."
    )

    valuation_assessment: str = Field(
        description="Assessment of the target valuation and whether it appears reasonable."
    )

    key_opportunities: list[str] = Field(
        description="Most important opportunities created by the acquisition."
    )

    key_risks: list[str] = Field(
        description="Most important risks that could affect the transaction."
    )

    regulatory_assessment: str = Field(
        description="Assessment of the regulatory and antitrust situation."
    )

    integration_assessment: str = Field(
        description="Assessment of the difficulty and feasibility of integration."
    )

    key_conditions: list[str] = Field(
        description="Conditions that should be satisfied before proceeding with the acquisition."
    )

    confidence: str = Field(
        description="Confidence level in the recommendation: High, Medium, or Low."
    )

    evidence_ids: list[str] = Field(
        default_factory=list
    )