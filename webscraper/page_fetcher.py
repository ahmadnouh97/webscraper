import requests
from abc import ABC, abstractmethod
from webscraper.proxy_manager import IProxyManager


class IPageFetcher(ABC):
    @abstractmethod
    def fetch(self, url):
        pass


class SimplePageFetcher(IPageFetcher):
    def fetch(self, url):
        response = requests.get(url)
        return response.text


class ProxyPageFetcher(IPageFetcher):
    def __init__(self, proxy_manager: IProxyManager):
        self.proxy_manager = proxy_manager

    def fetch(self, url):
        return self.proxy_manager.fetch_url_with_proxy(url)
