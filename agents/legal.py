from models.legal import LegalFinding
from state.schemas import AcquisitionState
from utils.legal_data import get_legal_information
from utils.llm import get_llm
from utils.evidence_factory import create_evidence


def legal_node(state: AcquisitionState):

    legal_information = get_legal_information(
        state.company_b
    )

    evidence_items = []

    if legal_information:

        evidence = create_evidence(
            source_name="Legal Intelligence Dataset",
            source_type="legal_data",
            content=str(legal_information),
            relevance=(
                f"Legal information retrieved for "
                f"{state.company_b}."
            ),
            credibility="medium",
        )

        evidence_items.append(evidence)

        evidence_id = evidence.evidence_id

    else:
        evidence_id = None

    llm = get_llm()

    structured_llm = llm.with_structured_output(
        LegalFinding,
        method="json_schema"
    )

    prompt = f"""
You are the Legal Due Diligence Agent
in an M&A intelligence system.

Acquiring Company:
{state.company_a}

Target Company:
{state.company_b}

User Question:
{state.user_question}

Available legal information:

{legal_information}

Analyze the available legal information.

Rules:

1. Use only the information provided.
2. Do not invent legal facts.
3. Identify the most important legal issue.
4. Explain why the issue matters.
5. Assess its severity as low, medium, or high.
6. Explain how it could affect the acquisition.
7. Do not treat potential disputes as confirmed
   legal judgments.
8. If information is unavailable, explicitly state that.
9. Produce one important legal finding.
"""

    finding = structured_llm.invoke(prompt)

    if evidence_id:
        finding.evidence_ids = [evidence_id]

    return {
        "legal_findings": [finding]
    }