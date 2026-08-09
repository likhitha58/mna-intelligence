from utils.news_data import get_company_news


def test_company_news():

    news = get_company_news("MSFT")

    print("\nCOMPANY NEWS\n")

    for item in news:
        print(f"Title: {item['title']}")
        print(f"Publisher: {item['publisher']}")
        print(f"URL: {item['url']}")
        print()


    assert isinstance(news, list)


if __name__ == "__main__":
    test_company_news()