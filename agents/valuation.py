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

    llm = get_llm()

    structured_llm = llm.with_structured_output(
        ValuationFinding,
        method="json_schema"
    )

    prompt = f"""
You are the Valuation Analyst Agent
in an M&A intelligence system.

Acquiring Company:
{state.company_a}

Target Company:
{state.company_b}

User Question:
{state.user_question}

IMPORTANT:

The target company may be privately held.

The valuation inputs below are ILLUSTRATIVE assumptions,
not verified financial statements.

DCF calculation:

{dcf_result}

Assumptions:

{assumptions}

Analyze the valuation output.

Rules:

1. Do not present the assumptions as verified company facts.
2. Clearly state that the valuation is illustrative.
3. Do not invent additional financial data.
4. Explain what the DCF result means for the acquisition.
5. Discuss the limitations of the valuation.
6. Assign an appropriate confidence level.
7. Produce one important valuation finding.

The estimated value should clearly indicate that
it is based on illustrative assumptions.
"""

    finding = structured_llm.invoke(prompt)

    finding.evidence_ids = [evidence.evidence_id]

    return {
        "valuation": finding
    }