from models.critic import CriticFeedback
from state.schemas import AcquisitionState
from utils.llm import get_llm


def critic_node(state: AcquisitionState):

    print("\n>>> CRITIC NODE STARTED")

    llm = get_llm()

    recommendation = state.committee_decision

    prompt = f"""
You are the Quality Control Critic Agent
in an M&A Intelligence Platform.

Your responsibility is to critically evaluate the
final acquisition recommendation approved by the
Investment Committee Agent after reviewing the Decision
Synthesis output.

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

FINAL RECOMMENDATION:
{recommendation}

COMMITTEE DECISION:

{recommendation}


KEY ANALYSIS SUMMARY:

Financial:
{state.financial_findings[-1] if state.financial_findings else "Unavailable"}

Valuation:
{state.valuation}

Risk:
{state.risks[-1] if state.risks else "Unavailable"}

Regulatory:
{state.regulatory_findings[-1] if state.regulatory_findings else "Unavailable"}

Synergy:
{state.synergies[-1] if state.synergies else "Unavailable"}

Integration:
{state.integration_findings[-1] if state.integration_findings else "Unavailable"}

Evidence Count:
{len(state.evidence)}


CRITIC EVALUATION CRITERIA:

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

9. Are the identified strategic synergies appropriately
   reflected in the recommendation, and are potential
   synergies distinguished from guaranteed benefits?

10. Are the evidence IDs consistent with the available
   evidence?

11. Is the confidence level justified by the quality
    and completeness of the evidence?

12. Identify important contradictions.

13. Identify important missing analysis.


APPROVAL RULE:

Set approved = true when the recommendation is
sufficiently supported by the available evidence.

Set approved = false only when there are important
problems that require the Decision Agent to reconsider
the recommendation.

Do NOT reject a recommendation merely because some
information is unavailable.

Instead, check whether the recommendation correctly
acknowledges that uncertainty.


LIST FIELD RULES:

major_issues MUST be a list.

missing_analysis MUST be a list.

evidence_issues MUST be a list.

recommended_changes MUST be a list.

If there are no items, return an empty list [].

NEVER return null.

Do not create any fields other than the fields
defined by the CriticFeedback schema.

The response must contain ONLY these fields:

approved
overall_assessment
major_issues
missing_analysis
evidence_issues
recommended_changes
confidence_assessment

Return ONLY valid JSON matching the CriticFeedback schema.

The JSON object must contain exactly these fields:
approved
overall_assessment
major_issues
missing_analysis
evidence_issues
recommended_changes
confidence_assessment

All list fields must be JSON arrays.
If there are no items, use [].
Never use null.
"""

    structured_llm = llm.with_structured_output(
        CriticFeedback,
        method="json_mode"
    )

    print(">>> CRITIC LLM CALL STARTING")

    feedback = structured_llm.invoke(prompt)

    print(">>> CRITIC LLM CALL COMPLETED")

    return {
        "critic_feedback": [feedback],
        "revision_count": 1
    }