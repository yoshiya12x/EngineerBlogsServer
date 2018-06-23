import requests
from bs4 import BeautifulSoup
import json
import re

url = "http://techlife.cookpad.com/archive/2018"
soup = BeautifulSoup(requests.get(url).content, 'html.parser')
articles = soup.find_all('section')
dataList = []

for article in articles:
    postDate = article.find("time").get("datetime")
    title = article.find("a", attrs={"class": "entry-title-link"}).string
    articleUrl = article.find("a", attrs={"class": "entry-title-link"}).get("href")
    imgElement = article.find("div", attrs={"class": "entry-thumb"})
    imgUrl = ""
    if imgElement is not None:
        imgUrl = re.search('(https?://.+)\);', imgElement.get("style")).group(1)
    author = ""

    dataList.append({
        "title": title,
        "articleUrl": articleUrl,
        "author": author,
        "imgUrl": imgUrl,
        "postDate": postDate
    })

print(json.dumps(dataList))
