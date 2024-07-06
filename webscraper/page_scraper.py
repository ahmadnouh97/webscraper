from html2text import HTML2Text


class PageScraper:
    def __init__(self, fetcher):
        self.fetcher = fetcher

    def scrape(self, url):
        html = self.fetcher.fetch(url)
        h = HTML2Text()
        h.ignore_links = True
        h.ignore_mailto_links = True
        h.ignore_images = True
        return h.handle(html)

