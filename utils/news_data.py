import yfinance as yf


def get_company_news(ticker: str, limit: int = 10) -> list[dict]:

    company = yf.Ticker(ticker)

    news = company.news[:limit]

    results = []

    for item in news:

        content = item.get("content", {})

        results.append(
            {
                "title": content.get("title"),
                "summary": content.get("summary"),
                "publisher": content.get("provider", {}).get("displayName"),
                "url": content.get("canonicalUrl", {}).get("url"),
                "published": content.get("pubDate"),
            }
        )

    return results