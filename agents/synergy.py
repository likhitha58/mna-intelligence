from models.synergy import SynergyFinding
from state.schemas import AcquisitionState
from utils.llm import get_llm
from utils.synergy_data import get_synergy_data
from utils.evidence_factory import create_evidence


def synergy_node(state: AcquisitionState) -> AcquisitionState:

    synergy_data = get_synergy_data(
        state.company_a,
        state.company_b
    )

    evidence_items = []

    if synergy_data:

        evidence = create_evidence(
            source_name="Strategic Synergy Dataset",
            source_type="synergy_data",
            content=str(synergy_data),
            relevance=(
                f"Strategic synergy information retrieved "
                f"for a potential combination of "
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
        SynergyFinding,
        method="json_schema"
    )

    prompt = f"""
You are the Strategic Synergy Analyst Agent
in an M&A intelligence system.

Acquiring Company:
{state.company_a}

Target Company:
{state.company_b}

User Question:
{state.user_question}

Potential synergy information:

{synergy_data}

Analyze the available information.

Rules:

1. Use only the information provided.
2. Do not invent financial values or guaranteed benefits.
3. Identify the most important potential synergy.
4. Explain why the combination could create additional value.
5. Distinguish potential value from guaranteed value.
6. Assess the difficulty of realizing the synergy.
7. Do not assume successful integration.
8. Produce one important synergy finding.
"""

    finding = structured_llm.invoke(prompt)

    if evidence_id:
        finding.evidence_ids = [evidence_id]

    return {
        "synergies": [finding],
        "evidence": evidence_items
    }