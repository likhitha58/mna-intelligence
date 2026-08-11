from models.integration import IntegrationFinding
from state.schemas import AcquisitionState
from utils.integration_data import get_integration_data
from utils.llm import get_llm
from utils.evidence_factory import create_evidence


def integration_node(state: AcquisitionState) -> AcquisitionState:

    integration_data = get_integration_data(
        state.company_a,
        state.company_b
    )

    evidence_items = []

    if integration_data:

        evidence = create_evidence(
            source_name="Integration Intelligence Dataset",
            source_type="integration_data",
            content=str(integration_data),
            relevance=(
                f"Integration information retrieved for "
                f"a potential combination of "
                f"{state.company_a} and {state.company_b}."
            ),
            credibility="medium",
        )

        evidence_items.append(evidence)

        evidence_id = evidence.evidence_id

    else:
        evidence_id = None

    llm = get_llm()

    structured_llm = llm.with_structured_output(
        IntegrationFinding
    )

    prompt = f"""
You are the Integration Planning Agent
in an M&A intelligence system.

Acquiring Company:
{state.company_a}

Target Company:
{state.company_b}

User Question:
{state.user_question}

Retrieved integration information:

{integration_data}

Analyze the available integration information.

Rules:

1. Use only the information provided.
2. Do not invent integration requirements.
3. Identify the most important integration area.
4. Estimate the integration timeline using the provided information.
5. Assess the integration difficulty.
6. Identify the most important actions required.
7. Consider technology, cloud infrastructure,
   security, organizational structure, and talent.
8. Do not present assumptions as confirmed facts.
9. Produce one important integration finding.
"""

    finding = structured_llm.invoke(prompt)

    if evidence_id:
        finding.evidence_ids = [evidence_id]

    return {
        "integration_findings": [finding],
        "evidence": evidence_items,
    }