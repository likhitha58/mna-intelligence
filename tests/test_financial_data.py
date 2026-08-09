from utils.financial_data import get_company_financials


def test_financial_data():

    data = get_company_financials("MSFT")

    print("\nFINANCIAL DATA\n")
    print(data)

    assert data["ticker"] == "MSFT"


if __name__ == "__main__":
    test_financial_data()