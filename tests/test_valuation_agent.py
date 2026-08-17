from agents.valuation import valuation_node
from state.schemas import AcquisitionState


def test_valuation_agent():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = valuation_node(state)

    print("\nVALUATION AGENT RESULT\n")
    print(result)

    assert "valuation" in result

    finding = result["valuation"]

    print("\nMETHOD:")
    print(finding.method)

    print("\nESTIMATED VALUE:")
    print(finding.estimated_value)

    print("\nASSUMPTIONS:")
    for assumption in finding.assumptions:
        print("-", assumption)

    print("\nINTERPRETATION:")
    print(finding.interpretation)

    print("\nCONFIDENCE:")
    print(finding.confidence)

    print("\nEVIDENCE IDS:")
    print(finding.evidence_ids)

    assert finding.evidence_ids
    assert finding.method == "DCF"


if __name__ == "__main__":
    test_valuation_agent()