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

TASK:
Produce exactly ONE competitive finding using ONLY the competitors provided.

RULES:
- Do not invent competitors or facts.
- Do not perform additional research.
- Identify the most important competitive threat.
- Explain why the competitor matters.
- Explain how the competitive situation could affect the acquisition.
- threat_level must be exactly one of:
  "low", "medium", or "high".
- If no competitors are available, explicitly state that
  information is unavailable.
- Keep the summary and impact concise.
- evidence_ids must be an empty list because evidence IDs
  are assigned by the application after the LLM response.

IMPORTANT:
Return a FLAT JSON object.

DO NOT create:
- a "properties" field
- a "description" field
- nested objects
- any additional fields

The response must contain EXACTLY these fields:

{{
    "competitor": "string",
    "threat_level": "medium",
    "summary": "string",
    "impact": "string",
    "evidence_ids": []
}}
"""

    finding = structured_llm.invoke(prompt)

    if evidence_id:
        finding.evidence_ids = [evidence_id]

    return {
        "competitor_findings": [finding]
    }