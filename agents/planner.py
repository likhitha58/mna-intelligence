from models.planner import ResearchPlan
from state.schemas import AcquisitionState
from utils.llm import get_llm


def create_research_plan(
    company_a: str,
    company_b: str,
    user_question: str
) -> ResearchPlan:

    llm = get_llm()

    structured_llm = llm.with_structured_output(ResearchPlan)

    prompt = f"""
You are the Research Planner for an M&A due diligence system.

The system is evaluating a potential acquisition.

Acquiring Company:
{company_a}

Target Company:
{company_b}

User Question:
{user_question}

Your task is to decompose the user's question into the research
tasks required for a comprehensive M&A investigation.

Consider relevant areas such as:

- Financial performance
- Market conditions
- Competitive landscape
- Legal and contractual issues
- Regulatory concerns
- Acquisition synergies
- Risks
- Valuation

Create specific and actionable research tasks.

Do not perform the analysis yourself.
Only create the research plan.
"""

    return structured_llm.invoke(prompt)


def planner_node(state: AcquisitionState) -> AcquisitionState:

    plan = create_research_plan(
        company_a=state.company_a,
        company_b=state.company_b,
        user_question=state.user_question
    )

    state.research_tasks = plan.tasks

    return state