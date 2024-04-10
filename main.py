"""
A simple example.
"""
from HPScraper import HPScraper
from playwright.sync_api._generated import Page

URL = 'https://www.kaufland.de/product/484770680/'
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"

def my_callback_function(page: Page):
    """
    scroll with the mouse a bit to ensure that every data is loaded
    some pages only load the wanted information if you interact with it
    all values in this loop are random feel free to change them or remove the loop
    """
    page.screenshot(path="screenshot.png")
    for i in range(3):
        page.mouse.wheel(0, 15000)
        
    print("my callback function called")
    

def main():
    scraper = HPScraper(user_agent=USER_AGENT)
    results = scraper.query_page_for_props(URL, ["price"], callback_function=my_callback_function)
    print(results)


if __name__ == '__main__':
    main()
