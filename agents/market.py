from models.market import MarketFinding
from state.schemas import AcquisitionState
from utils.llm import get_llm
from utils.news_data import get_company_news
from utils.evidence_factory import create_evidence


def market_node(state: AcquisitionState):

    news = get_company_news(state.company_b)

    evidence_items = []
    evidence_id = None

    if news:

        evidence = create_evidence(
            source_name="Yahoo Finance",
            source_type="news",
            content=str(news),
            relevance=(
                f"Recent market and news information "
                f"retrieved for {state.company_b}."
            ),
            credibility="medium",
        )

        evidence_items.append(evidence)
        evidence_id = evidence.evidence_id

    llm = get_llm()

    structured_llm = llm.with_structured_output(
        MarketFinding,
        method="json_schema"
    )

    prompt = f"""
You are the Market and News Intelligence Agent
in an M&A intelligence system.

Acquiring Company:
{state.company_a}

Target Company:
{state.company_b}

User Question:
{state.user_question}

Recent news about the target:

{news}

Analyze the available market and news information.

Rules:

1. Use only the information provided.
2. Do not invent news or events.
3. Identify the most important market development.
4. Explain how it could affect the acquisition.
5. Consider whether the signal is positive, negative, or neutral.
6. Do not treat rumors as confirmed facts.
7. If no useful news is available, explicitly state that.
8. Produce one important market finding.
"""

    finding = structured_llm.invoke(prompt)

    if evidence_id:
        finding.evidence_ids = [evidence_id]

    return {
        "market_findings": [finding],
        "evidence": evidence_items,
    }