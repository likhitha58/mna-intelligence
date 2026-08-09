from state.schemas import AcquisitionState


def main():

    state = AcquisitionState(
        company_a="Microsoft",
        company_b="OpenAI",
        user_question="Should Microsoft acquire OpenAI?"
    )

    print(state)


if __name__ == "__main__":
    main()