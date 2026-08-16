from models.regulatory import RegulatoryFinding
from state.schemas import AcquisitionState
from utils.llm import get_llm
from utils.regulatory_data import get_regulatory_data
from utils.evidence_factory import create_evidence


def regulatory_node(state: AcquisitionState) -> AcquisitionState:

    regulatory_data = get_regulatory_data(
        state.company_b
    )

    evidence_items = []

    if regulatory_data:

        evidence = create_evidence(
            source_name="Regulatory Intelligence Dataset",
            source_type="regulatory_data",
            content=str(regulatory_data),
            relevance=(
                f"Regulatory information retrieved "
                f"for {state.company_b}."
            ),
            credibility="medium",
        )

        evidence_items.append(evidence)

        evidence_id = evidence.evidence_id

    else:
        evidence_id = None

    llm = get_llm()

    structured_llm = llm.with_structured_output(
        RegulatoryFinding,
        method="json_schema"
    )

    prompt = f"""
You are the Regulatory and Compliance Agent
in an M&A intelligence system.

Acquiring Company:
{state.company_a}

Target Company:
{state.company_b}

User Question:
{state.user_question}

Retrieved regulatory information:
{regulatory_data}

TASK:
Produce exactly ONE regulatory finding using ONLY the information provided.

RULES:
- Do not invent regulations, laws, cases, jurisdictions, or regulatory actions.
- Do not perform additional research.
- Identify the most important regulatory risk.
- Identify the relevant jurisdiction.
- Explain how the regulatory issue could affect the acquisition.
- Do not treat potential regulatory scrutiny as confirmed regulatory action.
- If information is insufficient, explicitly state that.
- risk_level must be exactly one of:
  "low", "medium", or "high".
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
    "regulation": "string",
    "jurisdiction": "string",
    "risk_level": "medium",
    "summary": "string",
    "impact": "string",
    "evidence_ids": []
}}
"""

    finding = structured_llm.invoke(prompt)

    if evidence_id:
        finding.evidence_ids = [evidence_id]

    return {
        "regulatory_findings": [finding]
    }