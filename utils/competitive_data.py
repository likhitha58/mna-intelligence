def get_competitors(company: str) -> list[str]:

    known_competitors = {
        "OpenAI": [
            "Google",
            "Anthropic",
            "Meta",
            "xAI",
        ],
        "Microsoft": [
            "Google",
            "Amazon",
            "Apple",
            "Meta",
        ],
    }

    return known_competitors.get(
        company,
        []
    )