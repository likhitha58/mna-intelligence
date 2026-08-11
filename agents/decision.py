from models.recommendation import FinalRecommendation
from state.schemas import AcquisitionState
from utils.llm import get_llm


def decision_node(state: AcquisitionState):
    llm = get_llm()

    decision_context = {
        "acquiring_company": state.company_a,
        "target_company": state.company_b,
        "user_question": state.user_question,

        "financial_findings": state.financial_findings,
        "market_findings": state.market_findings,
        "competitive_findings": state.competitor_findings,
        "legal_findings": state.legal_findings,
        "regulatory_findings": state.regulatory_findings,

        "risks": state.risks,
        "valuation": state.valuation,
        "synergies": state.synergies,

        "integration_findings": getattr(
            state,
            "integration_findings",
            []
        ),

        "stakeholder_findings": getattr(
            state,
            "stakeholder_findings",
            []
        ),

        "evidence": state.evidence,
    }

    prompt = f"""
You are the Decision Synthesis Agent in an M&A Intelligence Platform.

Your responsibility is to make a final acquisition recommendation
based ONLY on the research findings already produced by the
specialized research agents.

You are NOT a research agent.

Do not perform new research.
Do not invent facts.
Do not invent financial information.
Do not fabricate evidence.

==================================================
ACQUISITION CONTEXT
==================================================

Acquiring Company:
{state.company_a}

Target Company:
{state.company_b}

User Question:
{state.user_question}

==================================================
RESEARCH FINDINGS
==================================================

{decision_context}

==================================================
DECISION RULES
==================================================

1. Evaluate the acquisition holistically.

2. Do NOT simply count positive and negative findings.

3. Consider the materiality of each finding.

4. A major regulatory, legal, financial, or integration
   risk may outweigh several minor positive factors.

5. Distinguish between verified information and assumptions.

6. If financial information is unavailable, explicitly state
   that it is unavailable. Never estimate missing financial
   facts unless the research findings explicitly provide them.

7. Treat illustrative valuation assumptions as illustrative.
   They must NOT be presented as verified market valuation.

8. Evaluate the strategic rationale of the acquisition.

9. Identify the strongest opportunities created by the deal.

10. Identify the most serious risks.

11. Evaluate regulatory and antitrust constraints.

12. Evaluate integration feasibility.

13. Consider stakeholder impact where available.

14. Recommend conditions that should be satisfied before
    proceeding.

15. Assign confidence based on the quality, completeness,
    and reliability of the available evidence.

16. Evidence IDs should only contain IDs that actually exist
    in the provided evidence.

==================================================
RECOMMENDATION
==================================================

The recommendation MUST be exactly one of:

- Proceed
- Proceed with Caution
- Do Not Proceed

Use:

Proceed
when the strategic and economic case is strong and major
risks appear manageable.

Proceed with Caution
when the acquisition has meaningful strategic value but
there are substantial risks, uncertainties, or conditions
that must be addressed.

Do Not Proceed
when major risks, poor economics, regulatory barriers,
strategic weakness, or other material concerns outweigh
the expected benefits.

==================================================
IMPORTANT
==================================================

Do not make the recommendation based solely on the number
of positive versus negative findings.

Prioritize materiality, evidence quality, strategic importance,
financial attractiveness, regulatory feasibility, and
integration risk.

Return a structured FinalRecommendation object.
"""

    structured_llm = llm.with_structured_output(
        FinalRecommendation
    )
    recommendation = structured_llm.invoke(prompt)
    return {
        "final_recommendation": recommendation
    }