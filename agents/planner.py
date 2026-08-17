from models.planner import ResearchPlan, ResearchTask
from state.schemas import AcquisitionState


def create_research_plan(
    company_a: str,
    company_b: str,
    user_question: str
) -> ResearchPlan:

    tasks = [

        ResearchTask(
            agent="Financial",
            objective=(
                f"Assess the available financial information "
                f"for {company_b}."
            )
        ),

        ResearchTask(
            agent="Market",
            objective=(
                f"Assess relevant market and news conditions "
                f"affecting {company_b}."
            )
        ),

        ResearchTask(
            agent="Competitive",
            objective=(
                f"Identify major competitors and competitive "
                f"threats facing {company_b}."
            )
        ),

        ResearchTask(
            agent="Legal",
            objective=(
                f"Identify major legal and intellectual-property "
                f"risks associated with {company_b}."
            )
        ),

        ResearchTask(
            agent="Regulatory",
            objective=(
                f"Assess major regulatory and antitrust risks "
                f"for the potential acquisition."
            )
        ),

        ResearchTask(
            agent="Risk",
            objective=(
                f"Identify the most important acquisition risks "
                f"associated with {company_b}."
            )
        ),

        ResearchTask(
            agent="Valuation",
            objective=(
                f"Assess the available valuation information "
                f"and key valuation assumptions for {company_b}."
            )
        ),

        ResearchTask(
            agent="Integration",
            objective=(
                f"Assess the major technology, organizational, "
                f"and operational integration requirements."
            )
        ),

        ResearchTask(
            agent="Stakeholder",
            objective=(
                f"Assess the most important stakeholder "
                f"implications of the acquisition."
            )
        ),

        ResearchTask(
            agent="Synergy",
            objective=(
                f"Identify the most important potential "
                f"strategic synergies between {company_a} and {company_b}."
            )
        ),
    ]

    return ResearchPlan(tasks=tasks)


def planner_node(state: AcquisitionState) -> AcquisitionState:

    plan = create_research_plan(
        company_a=state.company_a,
        company_b=state.company_b,
        user_question=state.user_question
    )

    state.research_tasks = plan.tasks

    return state