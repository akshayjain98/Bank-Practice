from pymongo import MongoClient


class ConnectionModel:
    @staticmethod
    def connect(collection_name):
        #without Authentication
        connection_url = MongoClient("localhost", 27017)
        return connection_url["aj_bank"][collection_name]
