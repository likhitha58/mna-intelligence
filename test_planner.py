from agents.planner import planner_node
from state.schemas import AcquisitionState


def main():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    updated_state = planner_node(state)

    print("\nRESEARCH TASKS\n")

    for task in updated_state.research_tasks:
        print(f"Agent: {task.agent}")
        print(f"Objective: {task.objective}")
        print()


if __name__ == "__main__":
    main()