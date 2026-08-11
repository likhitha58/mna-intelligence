from agents.integration import integration_node
from state.schemas import AcquisitionState


def test_integration_agent():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = integration_node(state)

    print("\nINTEGRATION FINDINGS\n")

    for finding in result["integration_findings"]:
        print(finding)

    print("\nEVIDENCE\n")

    for evidence in result["evidence"]:
        print(evidence)

    assert result["integration_findings"]
    assert result["evidence"]


if __name__ == "__main__":
    test_integration_agent()