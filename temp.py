from pymongo import MongoClient


client = MongoClient("mongodb://10.100.107.125:27017")
databases = client.database_names()

base = client['telejampiqDB']

coll = base['sensores'].find()

for i in coll:
    print i


