from models.recommendation import FinalRecommendation
from state.schemas import AcquisitionState
from utils.llm import get_llm


def decision_node(state: AcquisitionState):

    print("\n>>> DECISION NODE STARTED")

    llm = get_llm()

    latest_critic_feedback = (
        state.critic_feedback[-1]
        if state.critic_feedback
        else None
    )

    # --------------------------------------------------
    # Compact research context
    # --------------------------------------------------

    decision_context = {
        "financial_findings": state.financial_findings,
        "market_findings": state.market_findings,
        "competitive_findings": state.competitor_findings,
        "legal_findings": state.legal_findings,
        "regulatory_findings": state.regulatory_findings,
        "risks": state.risks,
        "valuation": state.valuation,
        "integration_findings": state.integration_findings,
        "stakeholder_findings": state.stakeholder_findings,
    }

    # --------------------------------------------------
    # Critic context
    # --------------------------------------------------

    critic_context = ""

    if latest_critic_feedback:

        critic_context = f"""
Previous Critic Feedback:

Approved:
{latest_critic_feedback.approved}

Overall Assessment:
{latest_critic_feedback.overall_assessment}

Major Issues:
{latest_critic_feedback.major_issues}

Missing Analysis:
{latest_critic_feedback.missing_analysis}

Evidence Issues:
{latest_critic_feedback.evidence_issues}

Recommended Changes:
{latest_critic_feedback.recommended_changes}

Confidence Assessment:
{latest_critic_feedback.confidence_assessment}
"""

    # --------------------------------------------------
    # Decision prompt
    # --------------------------------------------------

    prompt = f"""
You are the Decision Synthesis Agent in an M&A Intelligence Platform.

Your job is to produce the final acquisition recommendation.

You must use ONLY the research findings provided below.

Do NOT perform new research.

Do NOT invent facts.

Do NOT invent financial information.

Do NOT fabricate evidence.

Acquiring Company:
{state.company_a}

Target Company:
{state.company_b}

User Question:
{state.user_question}


RESEARCH FINDINGS:

{decision_context}


{critic_context}


DECISION RULES:

1. Evaluate the acquisition holistically.

2. Consider the materiality of each finding.

3. Do not simply count positive and negative findings.

4. Major regulatory, legal, financial, or integration
   risks can outweigh several minor benefits.

5. Clearly distinguish verified information from assumptions.

6. If financial information is unavailable, explicitly
   state that it is unavailable.

7. Never invent missing financial information.

8. If a valuation is illustrative, clearly describe it
   as illustrative.

9. Evaluate strategic rationale.

10. Identify the strongest opportunities.

11. Identify the strongest risks.

12. Evaluate regulatory and antitrust constraints.

13. Evaluate integration feasibility.

14. Consider stakeholder impact where available.

15. Recommend conditions that should be satisfied
    before proceeding.

16. Assign confidence based on evidence quality,
    completeness, and reliability.


RECOMMENDATION OPTIONS:

Proceed

Proceed with Caution

Do Not Proceed


Proceed:
Use when the strategic and economic case is strong
and major risks appear manageable.


Proceed with Caution:
Use when the acquisition has meaningful strategic
value but substantial risks or uncertainties must
be addressed.


Do Not Proceed:
Use when major risks, poor economics, regulatory
barriers, strategic weakness, or other material
concerns outweigh expected benefits.


CRITIC FEEDBACK:

If critic feedback is provided, use it to improve
the recommendation.

Do not blindly follow the critic.

Do not invent new information to address critic
comments.

If the critic identifies missing analysis that
cannot be resolved from the existing findings,
acknowledge the limitation rather than inventing
an answer.


IMPORTANT:

The final recommendation must be supported by the
available research.

The financial assessment must remain consistent
with the Financial Findings.

The valuation must remain consistent with the
Valuation Finding.

Do not present hypothetical assumptions as verified
financial facts.

Return a structured FinalRecommendation object as valid JSON.

The response must contain only valid JSON matching
the FinalRecommendation schema.
"""

    structured_llm = llm.with_structured_output(
        FinalRecommendation
    )

    print(">>> DECISION LLM CALL STARTING")

    recommendation = structured_llm.invoke(prompt)

    print(">>> DECISION LLM CALL COMPLETED")

    return {
        "final_recommendation": recommendation,
        "revision_count": state.revision_count + (
            1 if state.critic_feedback else 0
        ),
    }