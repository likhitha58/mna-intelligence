from state.schemas import AcquisitionState


def test_parallel_state():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    print("\nINITIAL STATE\n")
    print(state)

    assert state.financial_findings == []
    assert state.market_findings == []
    assert state.evidence == []

    print("\nParallel state schema is working.")


if __name__ == "__main__":
    test_parallel_state()