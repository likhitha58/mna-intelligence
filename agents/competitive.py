from models.competitive import CompetitiveFinding
from state.schemas import AcquisitionState
from utils.competitive_data import get_competitors
from utils.llm import get_llm
from utils.evidence_factory import create_evidence


def competitive_node(state: AcquisitionState):

    competitors = get_competitors(
        state.company_b
    )

    evidence_items = []

    if competitors:

        evidence = create_evidence(
            source_name="Competitive Intelligence Dataset",
            source_type="competitive_data",
            content=str(competitors),
            relevance=(
                f"Competitor information retrieved for "
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
        CompetitiveFinding,
        method="json_schema"
    )

    prompt = f"""
You are the Competitive Intelligence Agent
in an M&A intelligence system.

Acquiring Company:
{state.company_a}

Target Company:
{state.company_b}

User Question:
{state.user_question}

Known competitors of the target:

{competitors}

Analyze the competitive position of the target.

Rules:

1. Use only the competitors provided.
2. Do not invent competitors.
3. Identify the most important competitive threat.
4. Explain why the competitor matters.
5. Explain how the competitive situation could
   affect the acquisition.
6. Assign a threat level of low, medium, or high.
7. If no competitors are available, explicitly
   state that information is unavailable.
8. Produce one important competitive finding.
"""

    finding = structured_llm.invoke(prompt)

    if evidence_id:
        finding.evidence_ids = [evidence_id]

    return {
        "competitor_findings": [finding]
    }