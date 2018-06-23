import requests
from bs4 import BeautifulSoup
import json

url = 'https://inside.pixiv.blog/'
soup = BeautifulSoup(requests.get(url).content,'html.parser')
articles = soup.find_all('article')
dataList = []

for article in articles:
    articleUrl = article.find("a").get("href")
    title = article.find("h2").string
    author = article.find("div", attrs={"class": "article-list-item-author-name"}).string
    imgUrl = article.find("img").get("src")
    postDate = article.find("p", attrs={"class": "article-list-information-date"}).string

    dataList.append({
        "title": title.strip(),
        "articleUrl": articleUrl,
        "author": author.strip(),
        "imgUrl": imgUrl,
        "postDate": postDate.strip
    })

json.dumps(dataList)
