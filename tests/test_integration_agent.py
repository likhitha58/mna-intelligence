from agents.integration import integration_node
from state.schemas import AcquisitionState


def test_integration_agent():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = integration_node(state)

    print("\nINTEGRATION AGENT RESULT\n")
    print(result)

    assert "integration_findings" in result
    assert len(result["integration_findings"]) == 1

    finding = result["integration_findings"][0]

    print("\nINTEGRATION AREA:")
    print(finding.integration_area)

    print("\nTIMELINE:")
    print(finding.timeline)

    print("\nDIFFICULTY:")
    print(finding.difficulty)

    print("\nSUMMARY:")
    print(finding.summary)

    print("\nKEY ACTIONS:")
    for action in finding.key_actions:
        print("-", action)

    print("\nEVIDENCE IDS:")
    print(finding.evidence_ids)

    assert finding.evidence_ids


if __name__ == "__main__":
    test_integration_agent()