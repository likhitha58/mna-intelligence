from graph.workflow import build_graph
from state.schemas import AcquisitionState


def test_full_graph():

    print("\n" + "=" * 60)
    print("FULL M&A GRAPH TEST")
    print("=" * 60)

    initial_state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    graph = build_graph()

    result = graph.invoke(initial_state)

    print("\n" + "=" * 60)
    print("GRAPH COMPLETED")
    print("=" * 60)

    print("\nFINAL RECOMMENDATION:")

    if result.get("committee_decision"):
        decision = result["committee_decision"]

        print(
            f"Recommendation: "
            f"{decision.recommendation}"
        )

        print(
            f"Confidence: "
            f"{decision.confidence}"
        )

    else:
        print("No committee decision returned.")

    print("\nEVIDENCE:")

    evidence = result.get("evidence", [])

    print(
        f"Total evidence items: "
        f"{len(evidence)}"
    )

    for item in evidence:

        print(
            f"- {item.evidence_id} | "
            f"{item.source_name}"
        )

    print("\nFINDINGS:")

    print(
        "Financial:",
        len(result.get("financial_findings", []))
    )

    print(
        "Market:",
        len(result.get("market_findings", []))
    )

    print(
        "Competitive:",
        len(result.get("competitor_findings", []))
    )

    print(
        "Legal:",
        len(result.get("legal_findings", []))
    )

    print(
        "Regulatory:",
        len(result.get("regulatory_findings", []))
    )

    print(
        "Risk:",
        len(result.get("risks", []))
    )

    print(
        "Integration:",
        len(result.get("integration_findings", []))
    )

    print(
        "Stakeholder:",
        len(result.get("stakeholder_findings", []))
    )

    print(
        "Synergy:",
        len(result.get("synergies", []))
    )

    print(
        "Valuation:",
        "1" if result.get("valuation") else "0"
    )

    print(
        "\nRevision count:",
        result.get("revision_count", 0)
    )

    print(
        "Critic feedback:",
        len(result.get("critic_feedback", []))
    )

    print("\n" + "=" * 60)
    print("END OF TEST")
    print("=" * 60)


if __name__ == "__main__":
    test_full_graph()