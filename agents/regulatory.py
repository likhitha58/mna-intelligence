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

    llm = get_llm(max_tokens=900)

    structured_llm = llm.with_structured_output(
        RegulatoryFinding,
        method="json_schema"
    )

    prompt = f"""
You are an M&A regulatory analyst.

Acquirer: {state.company_a}
Target: {state.company_b}

Regulatory data:
{regulatory_data}

Create ONE concise regulatory finding.

Use ONLY the provided regulatory data.
Do not invent facts, laws, cases, or regulatory actions.

Rules:
- regulation: name the main regulatory issue
- jurisdiction: use a jurisdiction present in the data
- risk_level: exactly Low, Medium, or High
- summary: one concise sentence
- impact: one concise sentence
- evidence_ids: []

Return ONLY the structured RegulatoryFinding.
Do not provide explanations outside the structured output.
"""
    finding = structured_llm.invoke(prompt)

    if evidence_id:
        finding.evidence_ids = [evidence_id]

    return {
        "regulatory_findings": [finding],
        "evidence": evidence_items
    }