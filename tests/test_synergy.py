from agents.synergy import synergy_node
from state.schemas import AcquisitionState


def test_synergy_agent():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = synergy_node(state)

    print("\nSYNERGY FINDINGS\n")

    for finding in result["synergies"]:
        print(finding)

    print("\nEVIDENCE\n")

    for evidence in result["evidence"]:
        print(evidence)

    # ------------------------------------------
    # Basic validation
    # ------------------------------------------

    assert result["synergies"]
    assert len(result["synergies"]) == 1

    # ------------------------------------------
    # Validate synergy structure
    # ------------------------------------------

    finding = result["synergies"][0]

    assert finding.synergy_area
    assert finding.synergy_type
    assert finding.summary
    assert finding.potential_value
    assert finding.integration_difficulty

    # ------------------------------------------
    # Validate evidence
    # ------------------------------------------

    assert result["evidence"]

    # The synergy finding should reference evidence
    assert finding.evidence_ids

    print("\nSynergy Agent test passed!")


if __name__ == "__main__":
    test_synergy_agent()