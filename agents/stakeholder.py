from models.stakeholder import StakeholderFinding
from state.schemas import AcquisitionState
from utils.stakeholder_data import get_stakeholder_data
from utils.llm import get_llm
from utils.evidence_factory import create_evidence


def stakeholder_node(state: AcquisitionState) -> AcquisitionState:

    stakeholder_data = get_stakeholder_data(
        state.company_a,
        state.company_b
    )

    evidence_items = []

    if stakeholder_data:

        evidence = create_evidence(
            source_name="Stakeholder Intelligence Dataset",
            source_type="stakeholder_data",
            content=str(stakeholder_data),
            relevance=(
                f"Stakeholder impact information retrieved for "
                f"a potential combination of {state.company_a} "
                f"and {state.company_b}."
            ),
            credibility="medium",
        )

        evidence_items.append(evidence)

        evidence_id = evidence.evidence_id

    else:
        evidence_id = None

    llm = get_llm()

    structured_llm = llm.with_structured_output(
        StakeholderFinding,
        method="json_schema"
    )

    prompt = f"""
You are the Stakeholder Impact Analyst
in an M&A intelligence system.

Acquiring Company:
{state.company_a}

Target Company:
{state.company_b}

User Question:
{state.user_question}

Stakeholder information:

{stakeholder_data}

Analyze the stakeholder implications of the acquisition.

Rules:

1. Use only the information provided.
2. Do not invent stakeholder reactions.
3. Do not claim that stakeholders definitely support or oppose the deal.
4. Identify the most important stakeholder group.
5. Explain whether the impact is positive, negative, or neutral.
6. Assign an impact level: High, Medium, or Low.
7. Explain why the impact matters to the acquisition.
8. Produce one important stakeholder finding.
"""

    finding = structured_llm.invoke(prompt)

    if evidence_id:
        finding.evidence_ids = [evidence_id]

    return {
        "stakeholder_findings": [finding]
    }