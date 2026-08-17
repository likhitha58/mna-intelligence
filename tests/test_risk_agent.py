from agents.risk import risk_node
from state.schemas import AcquisitionState


def test_risk_agent():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = risk_node(state)

    print("\nRISK AGENT RESULT\n")
    print(result)

    assert "risks" in result
    assert len(result["risks"]) == 1

    finding = result["risks"][0]

    print("\nRISK AREA:")
    print(finding.risk_area)

    print("\nRISK LEVEL:")
    print(finding.risk_level)

    print("\nSUMMARY:")
    print(finding.summary)

    print("\nIMPACT:")
    print(finding.impact)

    print("\nMITIGATION:")
    print(finding.mitigation)

    print("\nEVIDENCE IDS:")
    print(finding.evidence_ids)


if __name__ == "__main__":
    test_risk_agent()