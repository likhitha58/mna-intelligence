from typing import Any

from pydantic import BaseModel, Field


class AcquisitionState(BaseModel):
    # Acquisition context
    company_a: str
    company_b: str
    user_question: str

    # Research planning
    research_tasks: list[Any] = Field(default_factory=list)

    # Agent findings
    financial_findings: list[Any] = Field(default_factory=list)
    market_findings: list[Any] = Field(default_factory=list)
    competitor_findings: list[Any] = Field(default_factory=list)
    legal_findings: list[Any] = Field(default_factory=list)
    regulatory_findings: list[Any] = Field(default_factory=list)

    # Cross-functional analysis
    synergies: list[Any] = Field(default_factory=list)
    risks: list[Any] = Field(default_factory=list)

    # Evidence
    evidence: list[Any] = Field(default_factory=list)

    # Valuation
    valuation: Any = None

    # Critic
    critic_feedback: list[Any] = Field(default_factory=list)

    # Final decision
    final_recommendation: Any = None