from webscraper.proxy_manager import ProxyManager
from webscraper.page_fetcher import SimplePageFetcher, ProxyPageFetcher
from webscraper.page_scraper import PageScraper
from webscraper.text_formatter import TextFormatter
from webscraper.page_cleaner import PageCleaner


def main():
    # Example usage:
    proxy_manager = ProxyManager()
    simple_fetcher = SimplePageFetcher()
    proxy_fetcher = ProxyPageFetcher(proxy_manager)

    scraper = PageScraper(proxy_fetcher)
    url = ""
    html_content = scraper.scrape(url)

    formatter = TextFormatter()
    cleaner = PageCleaner(formatter)
    cleaned_page, tags = cleaner.clean(html_content)

    with open("page.txt", "w", encoding="utf-8") as fp:
        fp.write(cleaned_page)

    print(f"tags = {tags}")


if __name__ == "__main__":
    main()