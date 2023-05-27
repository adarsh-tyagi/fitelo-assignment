from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from decouple import config
from CustomException import CustomException

class Database:
    '''
        This class is responsible for creating the database and collections in mongo db. This class needs the mongo atlas URI.
        Reads key 'uri' value from .env file in same path to create the mongo client.
    '''
    def createMongoDbAndCollection(self, db_name, collection_name):
        # reading uri from .env file, which have mongodb atlas uri to connect to the server
        uri = config("uri", default="")
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))

        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("You successfully connected to MongoDB!")
            db = client[db_name]
            # if collections already exist then delete it
            if collection_name in db.list_collection_names():
                db[collection_name].drop()
            # create collection
            collection = db[collection_name]
            print("Database and Collection are created successfully")
            return collection
        except Exception as e:
            print(e)
            return CustomException(e)
