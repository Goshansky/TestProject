from pymongo import MongoClient
from bson.objectid import ObjectId


class User:
    def __init__(self, mongo_uri='mongodb://localhost:27017', db_name='db', collection_name='users'):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create(self, full_name, login, password):
        user = {
            'full_name': full_name,
            'login': login,
            'password': password
        }
        result = self.collection.insert_one(user)
        return {'_id': str(result.inserted_id), **user}

    def find_one(self, query):
        result = self.collection.find_one(query)
        if result:
            result['_id'] = str(result['_id'])
            return result
        return None

    def find_all(self):
        results = []
        for user in self.collection.find():
            user['_id'] = str(user['_id'])
            results.append(user)
        return results

    def update(self, query, new_values):
        self.collection.update_one(query, {'$set': new_values})

    def delete(self, query):
        self.collection.delete_one(query)


user_manager = User()

# Create a new user
new_user = user_manager.create('John Doe', 'johndoe', 'password123')
print(new_user)

# Find a user by login
found_user = user_manager.find_one({'login': 'johndoe'})
print(found_user)

# Update a user's password
user_manager.update({'login': 'johndoe'}, {'password': 'new_password'})

# # Delete a user by login
# user_manager.delete({'login': 'johndoe'})