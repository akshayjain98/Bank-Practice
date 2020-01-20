from pymongo import MongoClient


class ConnectionModel:
    @staticmethod
    def connect(collection_name):
        #without Authentication
        #connection_url = MongoClient("localhost", 27017)


        #with authentication

        connection_url = MongoClient(host="localhost", username="akshay.jain", password="akshay123", port=27017)

        #connection_url = MongoClient("mongodb://akshay.jain:akshay123@localhost:27017/aj_bank?authSource=admin")

        #connection_url = MongoClient("mongodb://akshay.jain:akshay123@localhost:27017/")
        return connection_url["aj_bank"][collection_name]
