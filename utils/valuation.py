from typing import Any


def calculate_dcf(
    revenue: float,
    growth_rate: float,
    operating_margin: float,
    tax_rate: float,
    discount_rate: float,
    terminal_growth_rate: float,
    forecast_years: int = 5,
) -> dict[str, Any]:
    """
    Calculate a simplified DCF valuation.

    All calculations are deterministic and performed in Python.
    """

    projected_cash_flows = []

    current_revenue = revenue

    for year in range(1, forecast_years + 1):

        current_revenue *= (1 + growth_rate)

        operating_profit = current_revenue * operating_margin

        after_tax_profit = operating_profit * (1 - tax_rate)

        discounted_cash_flow = (
            after_tax_profit
            / ((1 + discount_rate) ** year)
        )

        projected_cash_flows.append(
            {
                "year": year,
                "revenue": current_revenue,
                "after_tax_profit": after_tax_profit,
                "discounted_cash_flow": discounted_cash_flow,
            }
        )

    terminal_cash_flow = (
        projected_cash_flows[-1]["after_tax_profit"]
        * (1 + terminal_growth_rate)
    )

    terminal_value = (
        terminal_cash_flow
        / (discount_rate - terminal_growth_rate)
    )

    discounted_terminal_value = (
        terminal_value
        / ((1 + discount_rate) ** forecast_years)
    )

    enterprise_value = (
        sum(
            year["discounted_cash_flow"]
            for year in projected_cash_flows
        )
        + discounted_terminal_value
    )

    return {
        "method": "DCF",
        "enterprise_value": enterprise_value,
        "projected_cash_flows": projected_cash_flows,
        "terminal_value": terminal_value,
        "discounted_terminal_value": discounted_terminal_value,
    }