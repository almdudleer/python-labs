from datetime import datetime, timezone

import pymongo
from bson.objectid import ObjectId
from flask import request
from flask_restful import Resource

from Lab6.util.db import mongo


class FeedEntries(Resource):
    def get(self, feed_id):
        from_date = request.args.get('fromDate')
        if from_date is not None:
            date = datetime.strptime(from_date, '%Y-%m-%dT%H:%M:%S%z')
        else:
            date = datetime.utcnow()
        entries = mongo.db.entries.find({
            'feedId': ObjectId(feed_id),
            'published': {'$lt': date}
        }, projection={'feedId': 0}, sort=[('published', pymongo.DESCENDING)], limit=9)

        entries = list(entries)

        for e in entries:
            e['published'] = e['published'].replace(tzinfo=timezone.utc).isoformat()

        return entries
