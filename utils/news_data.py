import yfinance as yf


def get_company_news(company: str, limit: int = 10) -> list[dict]:

    # --------------------------------------------------
    # Known private companies
    # --------------------------------------------------

    private_companies = {
        "openai"
    }

    if company.lower() in private_companies:

        return []


    # --------------------------------------------------
    # Public company news lookup
    # --------------------------------------------------

    try:

        company_obj = yf.Ticker(company)

        news = company_obj.news[:limit]

        results = []

        for item in news:

            content = item.get("content", {})

            results.append(
                {
                    "title": content.get("title"),
                    "summary": content.get("summary"),
                    "publisher": content.get(
                        "provider", {}
                    ).get("displayName"),
                    "url": content.get(
                        "canonicalUrl", {}
                    ).get("url"),
                    "published": content.get("pubDate"),
                }
            )

        return results

    except Exception:

        return []