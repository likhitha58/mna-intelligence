from agents.competitive import competitive_node
from state.schemas import AcquisitionState


def test_competitive_agent():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = competitive_node(state)

    print("\nCOMPETITIVE AGENT RESULT\n")
    print(result)

    assert "competitor_findings" in result
    assert len(result["competitor_findings"]) == 1

    finding = result["competitor_findings"][0]

    print("\nCOMPETITOR:")
    print(finding.competitor)

    print("\nTHREAT LEVEL:")
    print(finding.threat_level)

    print("\nSUMMARY:")
    print(finding.summary)

    print("\nIMPACT:")
    print(finding.impact)

    print("\nEVIDENCE IDS:")
    print(finding.evidence_ids)


if __name__ == "__main__":
    test_competitive_agent()