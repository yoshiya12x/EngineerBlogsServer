import requests
from bs4 import BeautifulSoup
import re

url = 'http://developers.gnavi.co.jp/'
soup = BeautifulSoup(requests.get(url).content,'html.parser')
articles = soup.find_all('article')
dataList = []

for article in articles:
    entryArticle = article.find("a", attrs={"class": "entry-title-link bookmark"})
    author = article.find("a", attrs={"class": re.compile("category-【執筆者】.+")}).string
    dataList.append({
        "title": entryArticle.string,
        "articleUrl": entryArticle.get("href"),
        "author": author,
        "imgUrl": article.find("img").get("src")
    })

print(dataList)

nextPageElement = soup.find("span", attrs={"class": "pager-next"})
nextPageUrl = nextPageElement.find("a").get("href")
print(nextPageUrl)
