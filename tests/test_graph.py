from graph.workflow import build_graph
from state.schemas import AcquisitionState


def test_market_graph():

    graph = build_graph()

    initial_state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    print("\nRunning full M&A workflow...\n")

    result = graph.invoke(initial_state)

    # ==================================================
    # Research Tasks
    # ==================================================

    print("\nRESEARCH TASKS\n")

    for task in result["research_tasks"]:
        print(
            f"{task.agent}: "
            f"{task.objective}"
        )

    assert result["research_tasks"]

    # ==================================================
    # Financial
    # ==================================================

    print("\nFINANCIAL FINDINGS\n")

    for finding in result["financial_findings"]:
        print(finding)

    assert result["financial_findings"]

    # ==================================================
    # Market
    # ==================================================

    print("\nMARKET FINDINGS\n")

    for finding in result["market_findings"]:
        print(finding)

    assert result["market_findings"]

    # ==================================================
    # Competitive
    # ==================================================

    print("\nCOMPETITIVE FINDINGS\n")

    for finding in result["competitor_findings"]:
        print(finding)

    assert result["competitor_findings"]

    # ==================================================
    # Legal
    # ==================================================

    print("\nLEGAL FINDINGS\n")

    for finding in result["legal_findings"]:
        print(finding)

    assert result["legal_findings"]

    # ==================================================
    # Regulatory
    # ==================================================

    print("\nREGULATORY FINDINGS\n")

    for finding in result["regulatory_findings"]:
        print(finding)

    assert result["regulatory_findings"]

    # ==================================================
    # Risk
    # ==================================================

    print("\nRISK FINDINGS\n")

    for finding in result["risks"]:
        print(finding)

    assert result["risks"]

    # ==================================================
    # Valuation
    # ==================================================

    print("\nVALUATION\n")

    print(result["valuation"])

    assert result["valuation"]

    # ==================================================
    # Integration
    # ==================================================

    print("\nINTEGRATION FINDINGS\n")

    for finding in result["integration_findings"]:
        print(finding)

    assert result["integration_findings"]

    # ==================================================
    # Stakeholders
    # ==================================================

    print("\nSTAKEHOLDER FINDINGS\n")

    for finding in result["stakeholder_findings"]:
        print(finding)

    assert result["stakeholder_findings"]
    
     # ==================================================
    # Synergy
    # ==================================================

    print("\nSYNERGY FINDINGS\n")

    for finding in result["synergies"]:
        print(finding)

    assert result["synergies"]

    # ==================================================
    # Final Recommendation
    # ==================================================

    print("\nFINAL RECOMMENDATION\n")

    committee_decision = result.get(
        "committee_decision"
    )
    assert committee_decision

    # ==================================================
    # Critic
    # ==================================================

    print("\nCRITIC FEEDBACK\n")

    critic_feedback = result.get(
        "critic_feedback"
    )

    print(critic_feedback)

    assert critic_feedback
    assert len(critic_feedback) > 0

    assert isinstance(
        critic_feedback[0].approved,
        bool
    )

    # ==================================================
    # Revision Count
    # ==================================================

    print("\nREVISION COUNT\n")

    print(
        result.get(
            "revision_count",
            0
        )
    )

    print(
        "\nFull M&A graph with "
        "Synergy + Committee + Critic passed!"
    )


if __name__ == "__main__":
    test_market_graph()