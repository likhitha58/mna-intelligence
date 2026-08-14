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

Analyze the available risk information.

Rules:

1. Use only the information provided.
2. Do not invent risks or facts.
3. Identify the most important risk.
4. Assign an appropriate risk level:
   Low, Medium, or High.
5. Explain the potential impact of the risk
   on the acquisition.
6. Suggest a practical mitigation strategy.
7. If information is unavailable, explicitly state that.
8. Produce one important risk finding.
"""

    finding = structured_llm.invoke(prompt)

    if evidence_id:
        finding.evidence_ids = [evidence_id]

    return {
        "risks": [finding]
    }