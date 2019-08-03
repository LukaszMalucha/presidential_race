from db import mongo


class Collection():

    def __init__(self):
        self.mongo = mongo

    def insert_data(self, data):
        return mongo.db.cadidates_odds.insert(data)

    @classmethod
    def find_last_data(cls, hashtag):
        return mongo.db.harvest_trends.find({"hashtag": hashtag})

