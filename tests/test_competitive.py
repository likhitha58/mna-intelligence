from agents.competitive import competitive_node
from state.schemas import AcquisitionState


def test_competitive_agent():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = competitive_node(state)

    print("\nCOMPETITIVE FINDINGS\n")

    for finding in result["competitor_findings"]:
        print(finding)

    print("\nEVIDENCE\n")

    for evidence in result["evidence"]:
        print(evidence)

    assert result["competitor_findings"]


if __name__ == "__main__":
    test_competitive_agent()