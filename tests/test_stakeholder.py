from agents.stakeholder import stakeholder_node
from state.schemas import AcquisitionState


def test_stakeholder_agent():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = stakeholder_node(state)

    print("\nSTAKEHOLDER FINDINGS\n")

    for finding in result["stakeholder_findings"]:
        print(finding)

    print("\nEVIDENCE\n")

    for evidence in result["evidence"]:
        print(evidence)

    assert result["stakeholder_findings"]
    assert result["evidence"]


if __name__ == "__main__":
    test_stakeholder_agent()