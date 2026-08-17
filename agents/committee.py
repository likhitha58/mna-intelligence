from models.committee import CommitteeDecision
from state.schemas import AcquisitionState
from utils.llm import get_llm


def committee_node(state: AcquisitionState) -> AcquisitionState:

    print("\n>>> COMMITTEE NODE STARTED")

    llm = get_llm(max_tokens=1000)

    structured_llm = llm.with_structured_output(
        CommitteeDecision,
        method="json_schema"
    )

    # ==========================================
    # MOST RECENT SPECIALIST FINDINGS
    # ==========================================

    financial = (
        state.financial_findings[-1]
        if state.financial_findings
        else "Unavailable"
    )

    market = (
        state.market_findings[-1]
        if state.market_findings
        else "Unavailable"
    )

    competitive = (
        state.competitor_findings[-1]
        if state.competitor_findings
        else "Unavailable"
    )

    legal = (
        state.legal_findings[-1]
        if state.legal_findings
        else "Unavailable"
    )

    regulatory = (
        state.regulatory_findings[-1]
        if state.regulatory_findings
        else "Unavailable"
    )

    risk = (
        state.risks[-1]
        if state.risks
        else "Unavailable"
    )

    valuation = (
        state.valuation
        if state.valuation
        else "Unavailable"
    )

    integration = (
        state.integration_findings[-1]
        if state.integration_findings
        else "Unavailable"
    )

    stakeholder = (
        state.stakeholder_findings[-1]
        if state.stakeholder_findings
        else "Unavailable"
    )

    synergy = (
        state.synergies[-1]
        if state.synergies
        else "Unavailable"
    )

    # ==========================================
    # COMPACT DECISION PROMPT
    # ==========================================

    prompt = f"""
You are the Investment Committee Agent.

Acquirer: {state.company_a}
Target: {state.company_b}
Question: {state.user_question}

Review these findings:

Financial:
{financial}

Market:
{market}

Competitive:
{competitive}

Legal:
{legal}

Regulatory:
{regulatory}

Risk:
{risk}

Valuation:
{valuation}

Integration:
{integration}

Stakeholder:
{stakeholder}

Synergy:
{synergy}

Make one evidence-based acquisition recommendation.

Rules:
- Use only the supplied findings.
- Do not invent facts.
- Treat unavailable data as unavailable.
- Treat the DCF valuation as illustrative.
- Consider both opportunities and risks.
- recommendation must be exactly:
  Proceed
  Proceed with Caution
  Do Not Proceed
- confidence must be exactly:
  Low
  Medium
  High
- Each list must contain at most 2 concise items.
- Keep all text fields concise.
- Return exactly one CommitteeDecision.
"""

    print(">>> COMMITTEE LLM CALL STARTING")

    decision = structured_llm.invoke(prompt)

    print(">>> COMMITTEE LLM CALL COMPLETED")

    return {
        "committee_decision": decision
    }