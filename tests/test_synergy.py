from agents.synergy import synergy_node
from state.schemas import AcquisitionState


def test_synergy_agent():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = synergy_node(state)

    print("\nSYNERGY FINDINGS\n")

    for finding in result["synergies"]:
        print(finding)

    print("\nEVIDENCE\n")

    for evidence in result["evidence"]:
        print(evidence)

    assert result["synergies"]


if __name__ == "__main__":
    test_synergy_agent()