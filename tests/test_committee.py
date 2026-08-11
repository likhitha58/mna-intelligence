from agents.committee import committee_node
from state.schemas import AcquisitionState


def test_committee_agent():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = committee_node(state)

    print("\nFINAL RECOMMENDATION\n")
    print(result.final_recommendation)

    assert result.final_recommendation is not None


if __name__ == "__main__":
    test_committee_agent()