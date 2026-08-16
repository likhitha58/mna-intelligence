from agents.market import market_node
from state.schemas import AcquisitionState


def test_market_agent():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = market_node(state)

    print("\nMARKET AGENT RESULT\n")
    print(result)

    assert "market_findings" in result
    assert len(result["market_findings"]) == 1

    finding = result["market_findings"][0]

    print("\nTOPIC:")
    print(finding.topic)

    print("\nSUMMARY:")
    print(finding.summary)

    print("\nIMPACT:")
    print(finding.impact)

    print("\nSENTIMENT:")
    print(finding.sentiment)

    print("\nEVIDENCE IDS:")
    print(finding.evidence_ids)


if __name__ == "__main__":
    test_market_agent()