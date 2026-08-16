from agents.regulatory import regulatory_node
from state.schemas import AcquisitionState


def test_regulatory_agent():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = regulatory_node(state)

    print("\nREGULATORY AGENT RESULT\n")
    print(result)

    assert "regulatory_findings" in result
    assert len(result["regulatory_findings"]) == 1

    finding = result["regulatory_findings"][0]

    print("\nREGULATION:")
    print(finding.regulation)

    print("\nJURISDICTION:")
    print(finding.jurisdiction)

    print("\nRISK LEVEL:")
    print(finding.risk_level)

    print("\nSUMMARY:")
    print(finding.summary)

    print("\nIMPACT:")
    print(finding.impact)

    print("\nEVIDENCE IDS:")
    print(finding.evidence_ids)


if __name__ == "__main__":
    test_regulatory_agent()