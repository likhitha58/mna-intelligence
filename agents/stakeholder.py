from models.stakeholder import StakeholderFinding
from state.schemas import AcquisitionState
from utils.stakeholder_data import get_stakeholder_data
from utils.llm import get_llm
from utils.evidence_factory import create_evidence


def stakeholder_node(state: AcquisitionState) -> AcquisitionState:

    # ==========================================
    # RETRIEVE STAKEHOLDER DATA
    # ==========================================

    stakeholder_data = get_stakeholder_data(
        state.company_a,
        state.company_b
    )

    evidence_items = []
    evidence_id = None

    # ==========================================
    # CREATE EVIDENCE
    # ==========================================

    if stakeholder_data:

        evidence = create_evidence(
            source_name="Stakeholder Intelligence Dataset",
            source_type="stakeholder_data",
            content=str(stakeholder_data),
            relevance=(
                f"Stakeholder impact information retrieved "
                f"for a potential combination of "
                f"{state.company_a} and {state.company_b}."
            ),
            credibility="medium",
        )

        evidence_items.append(evidence)
        evidence_id = evidence.evidence_id

    # ==========================================
    # LLM
    # ==========================================

    llm = get_llm(max_tokens=500)

    structured_llm = llm.with_structured_output(
        StakeholderFinding,
        method="json_schema"
    )

    # ==========================================
    # PROMPT
    # ==========================================

    prompt = f"""
You are an M&A stakeholder analyst.

Acquiring Company:
{state.company_a}

Target Company:
{state.company_b}

User Question:
{state.user_question}

Stakeholder information:
{stakeholder_data}

Analyze the information above and produce ONE stakeholder finding.

Rules:

1. Use only the provided information.
2. Do not invent stakeholder reactions.
3. Identify the most important stakeholder group.
4. impact_level must be High, Medium, or Low.
5. impact_type must be Positive, Negative, or Neutral.
6. Keep the summary concise.
7. Keep the implication concise.
8. evidence_ids must be an empty list.
9. Produce exactly one StakeholderFinding.
"""

    # ==========================================
    # STRUCTURED LLM CALL
    # ==========================================

    finding = structured_llm.invoke(prompt)

    # ==========================================
    # ATTACH EVIDENCE ID
    # ==========================================

    if evidence_id:
        finding.evidence_ids = [evidence_id]

    # ==========================================
    # RETURN
    # ==========================================

    return {
        "stakeholder_findings": [finding],
        "evidence": evidence_items
    }