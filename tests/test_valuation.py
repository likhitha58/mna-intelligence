from agents.valuation import valuation_node
from state.schemas import AcquisitionState


def test_valuation_agent():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = valuation_node(state)

    print("\nVALUATION\n")
    print(result["valuation"])

    print("\nEVIDENCE\n")

    for evidence in result["evidence"]:
        print(evidence)

    assert result["valuation"]
    assert result["evidence"]


if __name__ == "__main__":
    test_valuation_agent()