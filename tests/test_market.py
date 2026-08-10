from agents.market import market_node
from state.schemas import AcquisitionState


def test_market_agent():

    state = AcquisitionState(
        company_a="OpenAI",
        company_b="Microsoft",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = market_node(state)

    print("\nMARKET FINDINGS\n")

    for finding in result["market_findings"]:
        print(finding)

    print("\nEVIDENCE\n")

    for evidence in result["evidence"]:
        print(evidence)

    assert result["market_findings"]


if __name__ == "__main__":
    test_market_agent()