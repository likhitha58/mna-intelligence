from graph.workflow import build_graph
from state.schemas import AcquisitionState


def test_market_graph():

    graph = build_graph()

    initial_state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = graph.invoke(initial_state)

    print("\nRESEARCH TASKS\n")

    for task in result["research_tasks"]:
        print(
            f"{task.agent}: "
            f"{task.objective}"
        )

    print("\nFINANCIAL FINDINGS\n")

    for finding in result["financial_findings"]:
        print(finding)

    print("\nMARKET FINDINGS\n")

    for finding in result["market_findings"]:
        print(finding)

    assert result["research_tasks"]
    assert result["financial_findings"]
    assert result["market_findings"]
    
    print("\nCOMPETITIVE FINDINGS\n")

    for finding in result["competitor_findings"]:
        print(finding)
    assert result["competitor_findings"]
    
    print("\nLEGAL FINDINGS\n")

    for finding in result["legal_findings"]:
        print(finding)
    assert result["legal_findings"]
    
    print("\nREGULATORY FINDINGS\n")

    for finding in result["regulatory_findings"]:
        print(finding)

    assert result["regulatory_findings"]
    
    print("\nRISK FINDINGS\n")

    for finding in result["risks"]:
        print(finding)
        assert result["risks"]
        
    print("\nVALUATION\n")

    print(result["valuation"])

    assert result["valuation"]
    print("\nINTEGRATION FINDINGS\n")

    for finding in result["integration_findings"]:
        print(finding)

    assert result["integration_findings"]
    
    print("\nSTAKEHOLDER FINDINGS\n")

    for finding in result["stakeholder_findings"]:
        print(finding)

    assert result["stakeholder_findings"]
    
    print("\nFINAL RECOMMENDATION\n")
    print("Checking final recommendation...")

    final_recommendation = result.get("final_recommendation")
    print("Final recommendation retrieved.")
    print(final_recommendation)

if __name__ == "__main__":
    test_market_graph()