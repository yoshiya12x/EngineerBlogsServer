from collections import defaultdict
import feedparser
import datetime

def getRSS(self,page):
    rss_url = ["https://engineer.dena.jp/atom.xml",
    "https://dev.classmethod.jp/feed/",
    ]
    
    feed = []
    page_info = {
        "title": {},
        "link": {},
    }
    
    yesterday = datetime.datetime.utcnow().date() - datetime.timedelta(days=2)

    for url in rss_url:
       feed.extend(feedparser.parse(url).entries)

    for content in feed:
       content_updated_date = datetime.datetime(
           *content.updated_parsed[:6],
           tzinfo=datetime.timezone.utc
           )
       if content_updated_date.date() > yesterday:
           page_info = defaultdict(list)
           page_info["title"].append(content.title)
           page_info['link'].append(content.link)

    return page_info