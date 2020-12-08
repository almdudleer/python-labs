from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource

from Lab6.config import MONGO_URI
from Lab6.controller.feed_entries import FeedEntries
from Lab6.controller.feed_list import FeedList
from Lab6.controller.guess import Guess
from Lab6.util.db import mongo

app = Flask(__name__)
cors = CORS(app)
app.config["MONGO_URI"] = MONGO_URI
api = Api(app)
mongo.init_app(app)


class HelloWorld(Resource):
    def get(self, name, test):
        return {"data": "Hello World!" + name + test}


api.add_resource(FeedList, "/feed")
api.add_resource(FeedEntries, "/feed/<feed_id>/entries")
api.add_resource(Guess, "/guess")

if __name__ == "__main__":
    app.run(debug=True)
