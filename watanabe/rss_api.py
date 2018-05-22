from flask import Flask, jsonify, abort, make_response
from collections import defaultdict
import feedparser
import datetime

api = Flask(__name__)

@api.route('/getRSS/', methods=['GET'])
def getRSS():
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

    return make_response(jsonify(page_info))

@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3000)