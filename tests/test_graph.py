from graph.workflow import build_graph
from state.schemas import AcquisitionState


def test_planner_graph():

    graph = build_graph()

    initial_state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = graph.invoke(initial_state)

    print("\nFINAL STATE\n")
    print(result)

    assert result["research_tasks"]


if __name__ == "__main__":
    test_planner_graph()