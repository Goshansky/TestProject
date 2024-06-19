from pymongo import MongoClient
from bson.objectid import ObjectId


class Client:
    def __init__(self, mongo_uri='mongodb://localhost:27017', db_name='db', collection_name='clients'):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create(self, number, last_name, first_name, middle_name, date_of_birth, inn, responsible_full_name, status='Не в работе'):
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

# client_manager = Client()

# # Create a new client
# new_client = client_manager.create('Doe', 'John', 'Александрович', '1990-01-01', '123456789012', 'Ответственный ФИО', 'Не в работе')
# print(new_client)
#
# # Find a client by INN
# found_client = client_manager.find_one({'inn': '123456789012'})
# print(found_client)
#
# # Update a client's responsible_full_name
# client_manager.update({'inn': '123456789012'}, {'responsible_full_name': 'Новый Ответственный ФИО'})

# # Delete a client by INN
# client_manager.delete({'inn': '123456789012'})