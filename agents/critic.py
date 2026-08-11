from models.critic import CriticFeedback
from state.schemas import AcquisitionState
from utils.llm import get_llm


def critic_node(state: AcquisitionState):

    llm = get_llm()

    recommendation = state.final_recommendation

    prompt = f"""
You are the Quality Control Critic Agent
in an M&A Intelligence Platform.

Your responsibility is to critically evaluate the
final acquisition recommendation produced by the
Decision Synthesis Agent.

Do NOT perform new research.

Do NOT invent facts.

Do NOT introduce external information.

Evaluate ONLY the research findings and final
recommendation already present in the state.

Acquiring Company:
{state.company_a}

Target Company:
{state.company_b}

User Question:
{state.user_question}

Final Recommendation:
{recommendation}

Financial Findings:
{state.financial_findings}

Market Findings:
{state.market_findings}

Competitive Findings:
{state.competitor_findings}

Legal Findings:
{state.legal_findings}

Regulatory Findings:
{state.regulatory_findings}

Risk Findings:
{state.risks}

Valuation:
{state.valuation}

Integration Findings:
{state.integration_findings}

Stakeholder Findings:
{state.stakeholder_findings}

Evidence:
{state.evidence}

Evaluate the recommendation using the following criteria:

1. Is the recommendation supported by the findings?

2. Are the strongest risks reflected in the recommendation?

3. Are the strongest opportunities reflected?

4. Is the financial assessment consistent with the
   available financial information?

5. Is the valuation presented honestly as verified
   or illustrative?

6. Are regulatory and antitrust concerns appropriately
   reflected?

7. Are integration risks appropriately addressed?

8. Are stakeholder impacts considered where available?

9. Are the evidence IDs consistent with the available
   evidence?

10. Is the confidence level justified by the quality
    and completeness of the evidence?

11. Identify any important contradictions.

12. Identify any important missing analysis.

If the recommendation is sufficiently supported,
set approved to True.

If important problems exist that require the
Decision Agent to reconsider the recommendation,
set approved to False.

Do not reject a recommendation merely because
information is unavailable. Instead, determine
whether the recommendation appropriately acknowledges
that uncertainty.

Return a structured CriticFeedback object.
"""

    structured_llm = llm.with_structured_output(
        CriticFeedback
    )

    feedback = structured_llm.invoke(prompt)

    return {
        "critic_feedback": [feedback]
    }