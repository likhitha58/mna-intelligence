from agents.stakeholder import stakeholder_node
from state.schemas import AcquisitionState


def test_stakeholder_agent():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = stakeholder_node(state)

    print("\nSTAKEHOLDER AGENT RESULT\n")
    print(result)

    assert "stakeholder_findings" in result
    assert len(result["stakeholder_findings"]) == 1

    finding = result["stakeholder_findings"][0]

    print("\nSTAKEHOLDER GROUP:")
    print(finding.stakeholder_group)

    print("\nIMPACT LEVEL:")
    print(finding.impact_level)

    print("\nIMPACT TYPE:")
    print(finding.impact_type)

    print("\nSUMMARY:")
    print(finding.summary)

    print("\nIMPLICATION:")
    print(finding.implication)

    print("\nEVIDENCE IDS:")
    print(finding.evidence_ids)

    assert finding.evidence_ids


if __name__ == "__main__":
    test_stakeholder_agent()