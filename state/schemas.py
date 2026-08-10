from typing import Annotated, Any
from operator import add

from pydantic import BaseModel, Field

from models.evidence import Evidence
from models.financial import FinancialFinding
from models.market import MarketFinding
from models.competitive import CompetitiveFinding

class AcquisitionState(BaseModel):
    # Acquisition context
    company_a: str
    company_b: str
    user_question: str

    # Research planning
    research_tasks: list[Any] = Field(default_factory=list)

    # Agent findings
    financial_findings: Annotated[
    list[FinancialFinding],
    add
    ] = Field(default_factory=list)
    market_findings: Annotated[
    list[MarketFinding],
    add
    ] = Field(default_factory=list)
    competitor_findings: Annotated[
    list[CompetitiveFinding],
    add
    ] = Field(default_factory=list)
    legal_findings: Annotated[
    list[Any],
    add
    ] = Field(default_factory=list)
    regulatory_findings: Annotated[
    list[Any],
    add
    ] = Field(default_factory=list)

    # Cross-functional analysis
    synergies: list[Any] = Field(default_factory=list)
    risks: list[Any] = Field(default_factory=list)

    # Evidence
    evidence: Annotated[list[Evidence], add] = Field(
    default_factory=list
    )

    # Valuation
    valuation: Any = None

    # Critic
    critic_feedback: list[Any] = Field(default_factory=list)

    # Final decision
    final_recommendation: Any = None