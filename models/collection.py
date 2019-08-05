from db import mongo


class Collection():

    def __init__(self):
        self.mongo = mongo

    def insert_data(self, data):
        return mongo.db.candidates_odds.insert(data)

    @classmethod
    def distinct_dates(cls):
        return mongo.db.candidates_odds.distinct("date")

    @classmethod
    def find_random(cls):
        return mongo.db.candidates_odds.find_one()

    @classmethod
    def find_last_data(cls, date):
        return mongo.db.candidates_odds.find_one({'date': date})

    @classmethod
    def find_earliest_data(cls, date):
        return mongo.db.candidates_odds.find_one({'date': date})

    @classmethod
    def delete_by_date(cls, date):
        return mongo.db.candidates_odds.remove({"date": date})
