from agents.legal import legal_node
from state.schemas import AcquisitionState


def test_legal_agent():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = legal_node(state)

    print("\nLEGAL FINDINGS\n")

    for finding in result["legal_findings"]:
        print(finding)

    print("\nEVIDENCE\n")

    for evidence in result["evidence"]:
        print(evidence)

    assert result["legal_findings"]


if __name__ == "__main__":
    test_legal_agent()