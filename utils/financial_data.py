import yfinance as yf


def get_company_financials(ticker: str) -> dict:

    company = yf.Ticker(ticker)

    info = company.info

    return {
        "company_name": info.get("longName"),
        "ticker": ticker,
        "market_cap": info.get("marketCap"),
        "revenue": info.get("totalRevenue"),
        "net_income": info.get("netIncomeToCommon"),
        "total_assets": info.get("totalAssets"),
        "total_liabilities": info.get("totalLiabilitiesNetMinorityInterest"),
        "cash": info.get("totalCash"),
        "total_debt": info.get("totalDebt"),
    }