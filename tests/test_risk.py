from agents.risk import risk_node
from state.schemas import AcquisitionState


def test_risk_agent():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = risk_node(state)

    print("\nRISK FINDINGS\n")

    for finding in result["risks"]:
        print(finding)

    print("\nEVIDENCE\n")

    for evidence in result["evidence"]:
        print(evidence)

    assert result["risks"]


if __name__ == "__main__":
    test_risk_agent()