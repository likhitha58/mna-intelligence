from typing import Any


def get_risk_data(company: str) -> dict[str, Any]:
    """
    Return structured risk intelligence for the target company.
    """

    if company.lower() != "openai":
        return {
            "company_name": company,
            "risks": []
        }

    return {
        "company_name": company,
        "risks": {
            "talent_retention": (
                "Key AI researchers and engineers may leave following an acquisition."
            ),
            "technology": (
                "Integration of OpenAI's AI infrastructure and models into Microsoft's "
                "technology stack may create technical complexity."
            ),
            "integration": (
                "Differences in engineering processes, organizational structure, "
                "and decision-making could slow integration."
            ),
            "reputation": (
                "An acquisition could create reputational risks among OpenAI users, "
                "developers, researchers, and the broader AI ecosystem."
            ),
            "operational": (
                "Dependence on large-scale AI infrastructure and specialized systems "
                "could create operational challenges during integration."
            ),
            "geopolitical": (
                "AI technology may be affected by international restrictions, "
                "export controls, and geopolitical tensions."
            )
        }
    }