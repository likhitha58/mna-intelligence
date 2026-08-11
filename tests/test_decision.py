from agents.decision import decision_node
from state.schemas import AcquisitionState
from graph.workflow import build_graph


def main():

    print("Running research workflow...\n")

    graph = build_graph()

    initial_state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = graph.invoke(initial_state)

    print("Research workflow completed.")

    print("\nRunning Decision Synthesis...\n")

    decision_result = decision_node(
        AcquisitionState(**result)
    )

    recommendation = decision_result["final_recommendation"]

    print("\nFINAL RECOMMENDATION\n")

    print("Recommendation:")
    print(recommendation.recommendation)

    print("\nStrategic Rationale:")
    print(recommendation.strategic_rationale)

    print("\nFinancial Assessment:")
    print(recommendation.financial_assessment)

    print("\nValuation Assessment:")
    print(recommendation.valuation_assessment)

    print("\nKey Opportunities:")
    for opportunity in recommendation.key_opportunities:
        print("-", opportunity)

    print("\nKey Risks:")
    for risk in recommendation.key_risks:
        print("-", risk)

    print("\nRegulatory Assessment:")
    print(recommendation.regulatory_assessment)

    print("\nIntegration Assessment:")
    print(recommendation.integration_assessment)

    print("\nKey Conditions:")
    for condition in recommendation.key_conditions:
        print("-", condition)

    print("\nConfidence:")
    print(recommendation.confidence)

    print("\nEvidence:")
    for evidence_id in recommendation.evidence_ids:
        print("-", evidence_id)

    assert recommendation.recommendation in [
        "Proceed",
        "Proceed with Caution",
        "Do Not Proceed"
    ]

    assert recommendation.strategic_rationale
    assert recommendation.financial_assessment
    assert recommendation.valuation_assessment
    assert recommendation.regulatory_assessment
    assert recommendation.integration_assessment
    assert recommendation.confidence

    print("\nDecision synthesis with real research findings passed!")


if __name__ == "__main__":
    main()