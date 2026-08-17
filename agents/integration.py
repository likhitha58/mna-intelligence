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

    llm = get_llm(max_tokens=600)

    structured_llm = llm.with_structured_output(
    IntegrationFinding,
    method="json_schema"
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

TASK:
Produce exactly ONE integration finding using ONLY the information provided.

RULES:
- Do not invent integration requirements.
- Identify the most important integration area.
- Estimate the timeline only from the provided information.
- difficulty must be exactly one of:
  "Low", "Medium", or "High".
- Identify only the most important integration actions.
- Consider technology, cloud infrastructure, security,
  organizational structure, and talent only when supported
  by the provided information.
- Do not present assumptions as confirmed facts.
- Keep the summary concise.
- key_actions should contain only the most important actions.
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
    "integration_area": "string",
    "timeline": "string",
    "difficulty": "Medium",
    "summary": "string",
    "key_actions": ["string"],
    "evidence_ids": []
}}
"""

    finding = structured_llm.invoke(prompt)

    if evidence_id:
        finding.evidence_ids = [evidence_id]

    return {
        "integration_findings": [finding],
        "evidence": evidence_items
    }