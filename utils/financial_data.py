import yfinance as yf


def get_company_financials(company: str) -> dict:

    # --------------------------------------------------
    # Known private companies
    # --------------------------------------------------

    private_companies = {
        "openai"
    }

    if company.lower() in private_companies:

        return {
            "company_name": company,
            "ticker": None,
            "market_cap": None,
            "revenue": None,
            "net_income": None,
            "total_assets": None,
            "total_liabilities": None,
            "cash": None,
            "total_debt": None,
            "data_available": False,
            "reason": (
                "The company is privately held and "
                "public market financial data is unavailable."
            ),
        }

    # --------------------------------------------------
    # Public company lookup
    # --------------------------------------------------

    try:

        company_obj = yf.Ticker(company)

        info = company_obj.info

        financial_data = {
            "company_name": info.get("longName"),
            "ticker": company,
            "market_cap": info.get("marketCap"),
            "revenue": info.get("totalRevenue"),
            "net_income": info.get("netIncomeToCommon"),
            "total_assets": info.get("totalAssets"),
            "total_liabilities": info.get(
                "totalLiabilitiesNetMinorityInterest"
            ),
            "cash": info.get("totalCash"),
            "total_debt": info.get("totalDebt"),
        }

        has_data = any(
            value is not None
            for key, value in financial_data.items()
            if key not in {"company_name", "ticker"}
        )

        financial_data["data_available"] = has_data

        if not has_data:
            financial_data["reason"] = (
                "No usable public financial data was returned."
            )

        return financial_data

    except Exception as e:

        return {
            "company_name": company,
            "ticker": company,
            "market_cap": None,
            "revenue": None,
            "net_income": None,
            "total_assets": None,
            "total_liabilities": None,
            "cash": None,
            "total_debt": None,
            "data_available": False,
            "reason": (
                f"Financial data retrieval failed: {str(e)}"
            ),
        }