import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import OperationFailure

load_dotenv()
MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")


def get_mongodb_client() -> MongoClient:
    uri = f"mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@localhost:27017/"
    return MongoClient(uri)


def is_database_exist(client: MongoClient, dbname: str) -> bool:
    dbnames = client.list_database_names()
    if dbname in dbnames:
        return True
    return False


def is_collection_exist(database: Database, collection_name) -> bool:
    try:
        database.validate_collection(collection_name)
        return True
    except OperationFailure:
        print("Collection doesn't exist:", collection_name)
        return False
