from agents.legal import legal_node
from state.schemas import AcquisitionState


def test_legal_agent():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = legal_node(state)

    print("\nLEGAL AGENT RESULT\n")
    print(result)

    assert "legal_findings" in result
    assert len(result["legal_findings"]) == 1

    finding = result["legal_findings"][0]

    print("\nISSUE:")
    print(finding.issue)

    print("\nSEVERITY:")
    print(finding.severity)

    print("\nSUMMARY:")
    print(finding.summary)

    print("\nIMPACT:")
    print(finding.impact)

    print("\nEVIDENCE IDS:")
    print(finding.evidence_ids)


if __name__ == "__main__":
    test_legal_agent()