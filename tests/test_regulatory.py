from agents.regulatory import regulatory_node
from state.schemas import AcquisitionState


def test_regulatory_agent():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = regulatory_node(state)

    print("\nREGULATORY FINDINGS\n")

    for finding in result["regulatory_findings"]:
        print(finding)

    print("\nEVIDENCE\n")

    for evidence in result["evidence"]:
        print(evidence)

    assert result["regulatory_findings"]


if __name__ == "__main__":
    test_regulatory_agent()