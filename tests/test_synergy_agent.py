from agents.synergy import synergy_node
from state.schemas import AcquisitionState


def test_synergy_agent():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = synergy_node(state)

    print("\nSYNERGY AGENT RESULT\n")
    print(result)

    assert "synergies" in result
    assert len(result["synergies"]) == 1

    finding = result["synergies"][0]

    print("\nSYNERGY AREA:")
    print(finding.synergy_area)

    print("\nSYNERGY TYPE:")
    print(finding.synergy_type)

    print("\nSUMMARY:")
    print(finding.summary)

    print("\nPOTENTIAL VALUE:")
    print(finding.potential_value)

    print("\nINTEGRATION DIFFICULTY:")
    print(finding.integration_difficulty)

    print("\nEVIDENCE IDS:")
    print(finding.evidence_ids)

    assert finding.evidence_ids


if __name__ == "__main__":
    test_synergy_agent()