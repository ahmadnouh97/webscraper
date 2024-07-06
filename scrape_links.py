import requests
from bs4 import BeautifulSoup


def save_to_file(data, filepath: str):
    with open(filepath, "w", encoding="utf-8") as fp:
        fp.write(data)


url = ""
response = requests.get(url)


soup = BeautifulSoup(response.text, "html.parser")

articles = soup.select("article")

links = []
for article in articles:
    # find dive with "data-href" attr
    div = article.find("div", attrs={"data-href": True})
    article_link = div.get("data-href")
    links.append(article_link)

save_to_file("\n".join(links), "page.txt")
