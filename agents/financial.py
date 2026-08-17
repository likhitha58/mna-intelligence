from models.financial import FinancialFinding
from state.schemas import AcquisitionState
from utils.financial_data import get_company_financials
from utils.llm import get_llm
from utils.evidence_factory import create_evidence


def financial_node(state: AcquisitionState):

    financial_data = get_company_financials(
        state.company_b
    )

    evidence_items = []
    evidence_id = None

    has_financial_data = financial_data.get(
        "data_available",
        False
    )

    if has_financial_data:

        evidence = create_evidence(
            source_name="Yahoo Finance",
            source_type="market_data",
            content=str(financial_data),
            relevance=(
                f"Financial information retrieved for "
                f"{state.company_b}."
            ),
            credibility="medium",
        )

        evidence_items.append(evidence)
        evidence_id = evidence.evidence_id

    llm = get_llm()

    structured_llm = llm.with_structured_output(
        FinancialFinding,
        method="json_schema"
    )

    prompt = f"""
You are the Financial Analyst Agent in an M&A intelligence system.

Acquiring Company:
{state.company_a}

Target Company:
{state.company_b}

User Question:
{state.user_question}

Retrieved financial data:
{financial_data}

TASK:
Produce exactly ONE financial finding using ONLY the retrieved data.

RULES:
- Do not invent financial values.
- If financial information is unavailable, explicitly say "Unavailable".
- Do not perform additional research.
- Do not make assumptions about missing data.
- Keep the interpretation concise.
- evidence_ids must be an empty list because evidence IDs are assigned
  by the application after the LLM response.

IMPORTANT:
Return a FLAT JSON object.

DO NOT create:
- a "properties" field
- a "description" field
- nested objects
- any additional fields

The response must contain EXACTLY these fields:

{{
    "metric": "string",
    "value": "string",
    "period": "string",
    "interpretation": "string",
    "evidence_ids": []
}}
"""

    finding = structured_llm.invoke(prompt)

    if evidence_id:
        finding.evidence_ids = [evidence_id]

    return {
        "financial_findings": [finding],
        "evidence": evidence_items
    }