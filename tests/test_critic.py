from graph.workflow import build_graph
from agents.critic import critic_node
from state.schemas import AcquisitionState


def main():

    print("Running research workflow...\n")

    graph = build_graph()

    initial_state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    result = graph.invoke(initial_state)

    print("Research and decision workflow completed.")

    state = AcquisitionState(**result)

    print("\nRunning Critic...\n")

    critic_result = critic_node(state)

    feedback = critic_result["critic_feedback"][0]

    print("\nCRITIC FEEDBACK\n")

    print("Approved:")
    print(feedback.approved)

    print("\nOverall Assessment:")
    print(feedback.overall_assessment)

    print("\nMajor Issues:")
    for issue in feedback.major_issues:
        print("-", issue)

    print("\nMissing Analysis:")
    for item in feedback.missing_analysis:
        print("-", item)

    print("\nEvidence Issues:")
    for issue in feedback.evidence_issues:
        print("-", issue)

    print("\nRecommended Changes:")
    for change in feedback.recommended_changes:
        print("-", change)

    print("\nConfidence Assessment:")
    print(feedback.confidence_assessment)

    assert isinstance(feedback.approved, bool)
    assert feedback.overall_assessment
    assert feedback.confidence_assessment

    print("\nCritic test passed!")


if __name__ == "__main__":
    main()