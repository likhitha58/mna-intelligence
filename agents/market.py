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

TASK:
Produce exactly ONE market/news finding using ONLY the information provided.

RULES:
- Do not invent news, events, companies, dates, or facts.
- Do not perform additional research.
- Do not treat rumors as confirmed facts.
- If useful news is unavailable, explicitly state that.
- Keep the summary and impact concise.
- sentiment must be exactly one of:
  "positive", "negative", or "neutral".
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
    "topic": "string",
    "summary": "string",
    "impact": "string",
    "sentiment": "positive",
    "evidence_ids": []
}}
"""

    finding = structured_llm.invoke(prompt)

    if evidence_id:
        finding.evidence_ids = [evidence_id]

    return {
        "market_findings": [finding]
    }