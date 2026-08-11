from typing import Annotated, Any
from operator import add

from pydantic import BaseModel, Field

from models.evidence import Evidence
from models.financial import FinancialFinding
from models.market import MarketFinding
from models.competitive import CompetitiveFinding
from models.legal import LegalFinding
from models.risk import RiskFinding
from models.valuation import ValuationFinding
from models.integration import IntegrationFinding
from models.stakeholder import StakeholderFinding
from models.recommendation import FinalRecommendation
from models.critic import CriticFeedback


class AcquisitionState(BaseModel):

    # ==========================================
    # ACQUISITION CONTEXT
    # ==========================================

    company_a: str
    company_b: str
    user_question: str

    # ==========================================
    # RESEARCH PLANNING
    # ==========================================

    research_tasks: list[Any] = Field(
        default_factory=list
    )

    # ==========================================
    # AGENT FINDINGS
    # ==========================================

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
        list[LegalFinding],
        add
    ] = Field(default_factory=list)

    regulatory_findings: Annotated[
        list[Any],
        add
    ] = Field(default_factory=list)

    integration_findings: Annotated[
        list[IntegrationFinding],
        add
    ] = Field(default_factory=list)

    stakeholder_findings: Annotated[
        list[StakeholderFinding],
        add
    ] = Field(default_factory=list)

    # ==========================================
    # CROSS-FUNCTIONAL ANALYSIS
    # ==========================================

    synergies: list[Any] = Field(
        default_factory=list
    )

    risks: Annotated[
        list[RiskFinding],
        add
    ] = Field(default_factory=list)

    # ==========================================
    # EVIDENCE
    # ==========================================

    evidence: Annotated[
        list[Evidence],
        add
    ] = Field(default_factory=list)

    # ==========================================
    # VALUATION
    # ==========================================

    valuation: ValuationFinding | None = None

    # ==========================================
    # CRITIC
    # ==========================================

    critic_feedback: Annotated[
        list[CriticFeedback],
        add
    ] = Field(default_factory=list)

    revision_count: int = 0

    # ==========================================
    # FINAL DECISION
    # ==========================================

    final_recommendation: FinalRecommendation | None = None