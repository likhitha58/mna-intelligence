from models.committee import CommitteeDecision
from state.schemas import AcquisitionState
from utils.llm import get_llm


def committee_node(state: AcquisitionState) -> AcquisitionState:

    llm = get_llm()

    structured_llm = llm.with_structured_output(
        CommitteeDecision,
        method="json_schema"
    )

    prompt = f"""
You are the Investment Committee Agent in an M&A intelligence system.

Your responsibility is to make the final acquisition recommendation
after reviewing the findings produced by multiple specialist agents.

Acquiring Company:
{state.company_a}

Target Company:
{state.company_b}

User Question:
{state.user_question}


FINANCIAL FINDINGS:
{state.financial_findings}


MARKET FINDINGS:
{state.market_findings}


COMPETITIVE FINDINGS:
{state.competitor_findings}


LEGAL FINDINGS:
{state.legal_findings}


REGULATORY FINDINGS:
{state.regulatory_findings}


SYNERGY FINDINGS:
{state.synergies}


RISK FINDINGS:
{state.risks}


VALUATION:
{state.valuation}


INTEGRATION FINDINGS:
{getattr(state, "integration_findings", [])}


STAKEHOLDER FINDINGS:
{getattr(state, "stakeholder_findings", [])}


Instructions:

1. Consider all available findings together.

2. Do not invent facts, financial values, legal issues,
   regulatory developments, or market information.

3. Clearly distinguish between verified information,
   illustrative assumptions, and unavailable information.

4. Evaluate both strategic benefits and acquisition risks.

5. Pay particular attention to:
   - Financial attractiveness
   - Strategic synergies
   - Competitive threats
   - Legal risks
   - Regulatory risks
   - Talent and operational risks
   - Valuation reliability
   - Integration difficulty
   - Stakeholder impact

6. The valuation may be based on illustrative assumptions.
   Do not treat an illustrative valuation as verified financial data.

7. Produce one overall acquisition recommendation.

8. The recommendation should be one of:
   - Proceed
   - Proceed with Caution
   - Do Not Proceed

9. If major risks exist but the strategic opportunity remains
   attractive, prefer "Proceed with Caution" rather than automatically
   recommending "Do Not Proceed".

10. Provide practical conditions that should be satisfied before
    Microsoft proceeds with the acquisition.

11. Keep the recommendation evidence-based and balanced.

12. Return exactly one structured CommitteeDecision.
"""

    decision = structured_llm.invoke(prompt)

    state.final_recommendation = decision

    return state