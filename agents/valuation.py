from models.valuation import ValuationFinding
from state.schemas import AcquisitionState
from utils.llm import get_llm
from utils.valuation import calculate_dcf
from utils.evidence_factory import create_evidence


def valuation_node(state: AcquisitionState):

    # --------------------------------------------------
    # Temporary assumptions
    # --------------------------------------------------
    #
    # OpenAI is a private company and our current
    # financial data source does not provide complete
    # financial statements.
    #
    # Therefore, these are explicitly labeled as
    # illustrative assumptions rather than real
    # OpenAI financial figures.
    #

    assumptions = {
        "revenue": 10_000_000_000,
        "growth_rate": 0.30,
        "operating_margin": 0.20,
        "tax_rate": 0.21,
        "discount_rate": 0.10,
        "terminal_growth_rate": 0.03,
        "forecast_years": 5,
    }

    dcf_result = calculate_dcf(
        revenue=assumptions["revenue"],
        growth_rate=assumptions["growth_rate"],
        operating_margin=assumptions["operating_margin"],
        tax_rate=assumptions["tax_rate"],
        discount_rate=assumptions["discount_rate"],
        terminal_growth_rate=assumptions["terminal_growth_rate"],
        forecast_years=assumptions["forecast_years"],
    )

    # --------------------------------------------------
    # Create evidence
    # --------------------------------------------------

    evidence = create_evidence(
        source_name="Illustrative Valuation Assumptions",
        source_type="valuation_model",
        content=str(
            {
                "assumptions": assumptions,
                "dcf_result": dcf_result,
            }
        ),
        relevance=(
            f"Illustrative DCF valuation model prepared "
            f"for {state.company_b}."
        ),
        credibility="low",
    )

    # --------------------------------------------------
    # LLM interpretation
    # --------------------------------------------------

    llm = get_llm(max_tokens=400)

    structured_llm = llm.with_structured_output(
        ValuationFinding,
        method="json_schema"
    )

    prompt = f"""
Return one JSON object for the ValuationFinding schema.

Target: {state.company_b}

DCF enterprise value: {dcf_result["enterprise_value"]}

Key assumptions:
Revenue={assumptions["revenue"]}
Growth={assumptions["growth_rate"]}
Margin={assumptions["operating_margin"]}
Discount rate={assumptions["discount_rate"]}
Terminal growth={assumptions["terminal_growth_rate"]}

The valuation is illustrative and not based on verified financial statements.

Return ONLY valid JSON with exactly these fields:

{{
  "method": "DCF",
  "estimated_value": "illustrative enterprise value",
  "assumptions": ["key assumption 1", "key assumption 2"],
  "interpretation": "brief interpretation and limitation",
  "confidence": "low",
  "evidence_ids": []
}}
"""
    finding = structured_llm.invoke(prompt)

    finding.evidence_ids = [evidence.evidence_id]

    return {
        "valuation": finding,
        "evidence": [evidence]
    }