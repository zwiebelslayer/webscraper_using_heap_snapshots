from HPScraper import HPScraper

URL = 'https://www.amazon.de/dp/B06Y5VBFNB'
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"


def main():
    scraper = HPScraper(user_agent=USER_AGENT)
    results = scraper.query_page_for_props(URL, ["asin", "ourPrice"])
    print(results)


if __name__ == '__main__':
    main()
