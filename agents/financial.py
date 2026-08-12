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

Retrieved financial data for the target company:

{financial_data}

Analyze the available financial information.

Rules:

1. Use only the financial information provided.
2. Do not invent missing values.
3. If a value is missing, acknowledge that it is unavailable.
4. Explain what the financial metric means for the acquisition.
5. Produce one important financial finding.
"""

    finding = structured_llm.invoke(prompt)

    if evidence_id:
        finding.evidence_ids = [evidence_id]

    return {
        "financial_findings": [finding],
        "evidence": evidence_items,
    }