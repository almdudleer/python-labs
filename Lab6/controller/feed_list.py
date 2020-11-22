from datetime import datetime
from time import mktime

import feedparser
from bson import ObjectId
from flask import request
from flask_restful import Resource
from pymongo import ReturnDocument

from Lab6.util.db import mongo


class FeedList(Resource):
    def get(self):
        feeds = mongo.db.feed.find(projection={'entries': False})
        feeds = list(feeds)
        for feed in feeds:
            feed['_id'] = str(feed['_id'])
        return feeds

    def post(self):
        body = request.get_json(force=True)
        result = feedparser.parse(body['feedUrl'])
        feedId = create_or_update_feed(result)
        update_feed_items(feedId, result['entries'])

    def patch(self):
        body = request.get_json(force=True)
        feed = mongo.db.feed.find_one({'_id': ObjectId(body['feedId'])})
        result = feedparser.parse(feed['href'])
        feedId = create_or_update_feed(result)
        update_feed_items(feedId, result['entries'])


def create_or_update_feed(rss):
    feed = mongo.db.feed.find_one_and_update({
        'href': rss['href']
    }, {
        '$set': {
            'title': rss['feed']['title'],
            'href': rss['href'],
            'image': rss['feed']['image']['href']
        }
    },
        projection={'_id': True},
        upsert=True,
        return_document=ReturnDocument.AFTER
    )
    return feed['_id']


def update_feed_items(feedId, entries):
    for entry in entries:
        image = next((x for x in entry['links'] if x['type'].startswith('image')), {'href': None})
        struct = entry['published_parsed']
        dt = datetime.fromtimestamp(mktime(struct))
        mongo.db.entries.update_one({
            '_id': entry['id'],
        }, {
            '$set': {
                '_id': entry['id'],
                'title': entry['title'],
                'href': entry['link'],
                'published': dt,
                'image': image['href'],
                'summary': entry.get('summary', ''),
                'feedId': feedId
            }
        }, upsert=True)
