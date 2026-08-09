from graph.workflow import build_graph
from state.schemas import AcquisitionState


def test_market_graph():

    graph = build_graph()

    initial_state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = graph.invoke(initial_state)

    print("\nRESEARCH TASKS\n")

    for task in result["research_tasks"]:
        print(
            f"{task.agent}: "
            f"{task.objective}"
        )

    print("\nFINANCIAL FINDINGS\n")

    for finding in result["financial_findings"]:
        print(finding)

    print("\nMARKET FINDINGS\n")

    for finding in result["market_findings"]:
        print(finding)

    assert result["research_tasks"]
    assert result["financial_findings"]
    assert result["market_findings"]


if __name__ == "__main__":
    test_market_graph()