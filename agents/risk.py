from models.risk import RiskFinding
from state.schemas import AcquisitionState
from utils.risk_data import get_risk_data
from utils.llm import get_llm
from utils.evidence_factory import create_evidence


def risk_node(state: AcquisitionState):

    risk_data = get_risk_data(state.company_b)

    evidence_items = []
    evidence_id = None

    if risk_data.get("risks"):

        evidence = create_evidence(
            source_name="Risk Intelligence Dataset",
            source_type="risk_data",
            content=str(risk_data),
            relevance=(
                f"Risk information retrieved for "
                f"{state.company_b}."
            ),
            credibility="medium",
        )

        evidence_items.append(evidence)
        evidence_id = evidence.evidence_id

    llm = get_llm()

    structured_llm = llm.with_structured_output(
        RiskFinding,
        method="json_schema"
    )

    prompt = f"""
You are the Risk Management Agent
in an M&A intelligence system.

Acquiring Company:
{state.company_a}

Target Company:
{state.company_b}

User Question:
{state.user_question}

Retrieved risk information:
{risk_data}

TASK:
Produce exactly ONE risk finding using ONLY the information provided.

RULES:
- Do not invent risks or facts.
- Identify the most important risk.
- risk_level must be exactly one of:
  "low", "medium", or "high".
- Explain the potential impact on the acquisition.
- Suggest one practical mitigation strategy.
- If information is unavailable, explicitly state that.
- Keep the summary, impact, and mitigation concise.
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
    "risk_area": "string",
    "risk_level": "medium",
    "summary": "string",
    "impact": "string",
    "mitigation": "string",
    "evidence_ids": []
}}
"""

    finding = structured_llm.invoke(prompt)

    if evidence_id:
        finding.evidence_ids = [evidence_id]

    return {
        "risks": [finding],
        "evidence": evidence_items
    }