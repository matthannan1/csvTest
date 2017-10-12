import pymongo
from pymongo import MongoClient

client = MongoClient()

# Get the sampleDB database
db = client.ftdna