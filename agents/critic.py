from models.critic import CriticFeedback
from state.schemas import AcquisitionState
from utils.llm import get_llm


def critic_node(state: AcquisitionState):

    print("\n>>> CRITIC NODE STARTED")

    llm = get_llm(max_tokens=500)

    structured_llm = llm.with_structured_output(
        CriticFeedback,
        method="json_schema"
    )

    # ==========================================
    # MOST RECENT FINDINGS
    # ==========================================

    financial = (
        state.financial_findings[-1]
        if state.financial_findings
        else "Unavailable"
    )

    valuation = (
        state.valuation
        if state.valuation
        else "Unavailable"
    )

    risk = (
        state.risks[-1]
        if state.risks
        else "Unavailable"
    )

    regulatory = (
        state.regulatory_findings[-1]
        if state.regulatory_findings
        else "Unavailable"
    )

    synergy = (
        state.synergies[-1]
        if state.synergies
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

    recommendation = state.committee_decision

    # ==========================================
    # CRITIC PROMPT
    # ==========================================

    prompt = f"""
You are the Quality Control Critic Agent in an M&A intelligence system.

Evaluate the Investment Committee recommendation using ONLY the
information already present below.

Do NOT perform new research.
Do NOT use external information.
Do NOT invent facts.

ACQUIRER:
{state.company_a}

TARGET:
{state.company_b}

USER QUESTION:
{state.user_question}

COMMITTEE RECOMMENDATION:
{recommendation}

FINANCIAL:
{state.financial_findings[-1] if state.financial_findings else "Unavailable"}

VALUATION:
{state.valuation}

RISK:
{state.risks[-1] if state.risks else "Unavailable"}

REGULATORY:
{state.regulatory_findings[-1] if state.regulatory_findings else "Unavailable"}

SYNERGY:
{state.synergies[-1] if state.synergies else "Unavailable"}

INTEGRATION:
{state.integration_findings[-1] if state.integration_findings else "Unavailable"}

STAKEHOLDER:
{state.stakeholder_findings[-1] if state.stakeholder_findings else "Unavailable"}

EVIDENCE COUNT:
{len(state.evidence)}

Evaluate these questions:

1. Is the recommendation supported by the available findings?
2. Are major risks reflected?
3. Are important opportunities reflected?
4. Is the financial assessment consistent with available information?
5. Is the valuation clearly identified as illustrative when appropriate?
6. Are regulatory concerns reflected?
7. Are integration concerns reflected?
8. Is confidence justified by the evidence?

APPROVAL RULE:

approved = true if the recommendation is reasonably supported
by the available evidence.

approved = false only if an important problem requires
the recommendation to be reconsidered.

Do not reject the recommendation merely because some information
is unavailable if the recommendation acknowledges that uncertainty.

OUTPUT RULES:

Return exactly one CriticFeedback object.

approved must be true or false.

major_issues must be a JSON array.
missing_analysis must be a JSON array.
evidence_issues must be a JSON array.
recommended_changes must be a JSON array.

Use [] when there are no items.

Keep every text field concise.

Do not create additional fields.
Do not return null.

Return only the structured CriticFeedback output.
"""

    print(">>> CRITIC LLM CALL STARTING")

    feedback = structured_llm.invoke(prompt)

    print(">>> CRITIC LLM CALL COMPLETED")

    return {
        "critic_feedback": [feedback],
        "revision_count": 1
    }