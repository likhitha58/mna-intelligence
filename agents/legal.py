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

TASK:
Produce exactly ONE legal finding using ONLY the information provided.

RULES:
- Do not invent legal facts.
- Do not perform additional research.
- Identify the most important legal issue.
- Explain why the issue matters.
- severity must be exactly one of:
  "low", "medium", or "high".
- Explain how the issue could affect the acquisition.
- Do not treat potential disputes as confirmed legal judgments.
- If information is unavailable, explicitly state that.
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
    "issue": "string",
    "severity": "medium",
    "summary": "string",
    "impact": "string",
    "evidence_ids": []
}}
"""

    finding = structured_llm.invoke(prompt)

    if evidence_id:
        finding.evidence_ids = [evidence_id]

    return {
        "legal_findings": [finding]
    }