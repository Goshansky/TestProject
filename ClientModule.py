from pymongo import MongoClient


class Client:
    def __init__(self, mongo_uri='mongodb://localhost:27017', db_name='db', collection_name='clients'):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create(self, number, last_name, first_name, middle_name, date_of_birth, inn, responsible_full_name,
               status='Не в работе'):
        client = {
            'number': number,
            'last_name': last_name,
            'first_name': first_name,
            'middle_name': middle_name,
            'date_of_birth': date_of_birth,
            'inn': inn,
            'responsible_full_name': responsible_full_name,
            'status': status
        }
        result = self.collection.insert_one(client)
        return {'_id': str(result.inserted_id), **client}

    def find_one(self, query):
        result = self.collection.find_one(query)
        if result:
            result['_id'] = str(result['_id'])
            return result
        return None

    def find_all(self):
        results = []
        for client in self.collection.find():
            client['_id'] = str(client['_id'])
            results.append(client)
        return results

    def update(self, query, new_values):
        self.collection.update_one(query, {'$set': new_values})

    def delete(self, query):
        self.collection.delete_one(query)

    def find(self, query):
        """Находит документы в коллекции по заданному запросу."""
        cursor = self.collection.find(query)
        return cursor
