from pydantic import BaseModel, Field


class CriticFeedback(BaseModel):

    approved: bool = Field(
        description=(
            "Whether the final recommendation is sufficiently "
            "supported by the available research."
        )
    )

    overall_assessment: str = Field(
        description=(
            "Overall assessment of the quality, consistency, "
            "and evidence support of the recommendation."
        )
    )

    major_issues: list[str] = Field(
        default_factory=list,
        description=(
            "Major issues that could make the recommendation "
            "unreliable or inconsistent."
        )
    )

    missing_analysis: list[str] = Field(
        default_factory=list,
        description=(
            "Important areas that are missing or insufficiently "
            "addressed in the recommendation."
        )
    )

    evidence_issues: list[str] = Field(
        default_factory=list,
        description=(
            "Problems involving evidence quality or evidence IDs."
        )
    )

    recommended_changes: list[str] = Field(
        default_factory=list,
        description=(
            "Specific changes that should be made if the "
            "recommendation requires revision."
        )
    )

    confidence_assessment: str = Field(
        description=(
            "Assessment of whether the stated confidence level "
            "is justified."
        )
    )