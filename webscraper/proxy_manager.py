# webscraper/proxy_manager.py
import requests
from itertools import cycle
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod


class IProxyManager(ABC):
    @abstractmethod
    def fetch_url_with_proxy(self, url):
        pass


class ProxyManager(IProxyManager):
    def __init__(self):
        self.proxies = self.get_free_proxies()
        self.proxy_pool = cycle(self.proxies)

    def fetch_url_with_proxy(self, url):
        proxy = next(self.proxy_pool)
        proxies = {
            "http": proxy,
            # "https": proxy
        }
        response = requests.get(url, proxies=proxies)
        return response.text

    def get_free_proxies(self):
        url = "https://free-proxy-list.net/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        proxies = []

        for row in soup.find("table", {"class": "table"}).find_all("tr"):
            cols = row.find_all("td")
            if cols and cols[6].text.strip() == "yes":
                proxy = f"http://{cols[0].text.strip()}:{cols[1].text.strip()}"
                proxies.append(proxy)
        return proxies


# if __name__ == "__main__":
#     manager = ProxyManager()
#     url = ""
#     print(manager.fetch_url_with_proxy(url))
