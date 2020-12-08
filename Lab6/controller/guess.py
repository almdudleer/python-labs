import random
from datetime import datetime

import requests
from bson import ObjectId
from flask import request
from flask_restful import Resource

from Lab6.util.db import mongo


class Guess(Resource):
    def get(self):
        with open("famous.txt") as file:
            people = file.read().splitlines()
        selected_people = random.sample(people, int(request.args.get('optionsCount')))
        r = requests.get("https://api.qwant.com/api/search/images", params={
            'count': 50,
            'q': selected_people[0],
            't': 'images',
            'safesearch': 1,
            'locale': 'en_US',
            'uiv': 4
        }, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        })
        print(r.json())
        image = random.choice(r.json()['data']['result']['items'])['media']
        insert_result = mongo.db.guess.insert_one({
            'createdAt': datetime.utcnow(),
            'answer': selected_people[0]
        })
        random.shuffle(selected_people)
        return {
            'id': str(insert_result.inserted_id),
            'names': selected_people,
            'image': image
        }

    def post(self):
        body = request.get_json(force=True)
        task = mongo.db.guess.find_one({'_id': ObjectId(body['taskId'])})
        if task is not None:
            if task['answer'] == body['answer']:
                return {
                    'result': True
                }
            else:
                return {
                    'result': False,
                    'answer': task['answer']
                }
        else:
            return None, 404
