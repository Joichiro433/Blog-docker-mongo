from pymongo import MongoClient


HOST = 'localhost'
PORT = 27017
USERNAME = 'root'
PASSWORD = 'password'

DB_NAME = 'demo_db'
COLLECTION_NAME = 'demo_collection'


if __name__ == '__main__':
    client = MongoClient(host=HOST, port=PORT, username=USERNAME, password=PASSWORD)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    data = [
        {'username': 'Alice', 'score': 100},
        {'username': 'Bob', 'score': 90}
    ]
    collection.insert_many(data)
    