def get_legal_information(company: str) -> dict:

    known_information = {
        "OpenAI": {
            "contracts": [
                "Strategic partnership agreements",
                "Cloud infrastructure agreements"
            ],
            "intellectual_property": [
                "AI model intellectual property",
                "Research and training technology"
            ],
            "litigation": [
                "Potential copyright and intellectual property disputes"
            ],
            "licensing": [
                "Model and technology licensing arrangements"
            ]
        },

        "Microsoft": {
            "contracts": [
                "Enterprise customer agreements",
                "Cloud service agreements"
            ],
            "intellectual_property": [
                "Microsoft software and cloud technology IP"
            ],
            "litigation": [],
            "licensing": [
                "Software and technology licensing agreements"
            ]
        }
    }

    return known_information.get(
        company,
        {}
    )