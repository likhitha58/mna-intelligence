from agents.financial import financial_node
from state.schemas import AcquisitionState


def test_financial_agent():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = financial_node(state)

    print("\nFINANCIAL AGENT RESULT\n")
    print(result)

    assert "financial_findings" in result
    assert len(result["financial_findings"]) == 1

    finding = result["financial_findings"][0]

    print("\nMETRIC:")
    print(finding.metric)

    print("\nVALUE:")
    print(finding.value)

    print("\nPERIOD:")
    print(finding.period)

    print("\nINTERPRETATION:")
    print(finding.interpretation)

    print("\nEVIDENCE IDS:")
    print(finding.evidence_ids)


if __name__ == "__main__":
    test_financial_agent()