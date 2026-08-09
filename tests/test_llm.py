from utils.llm import get_llm


def main():
    llm = get_llm()

    response = llm.invoke(
        "Explain in one sentence what an acquisition is."
    )

    print(response.content)


if __name__ == "__main__":
    main()