from pymongo import MongoClient

client = MongoClient("mongodb://10.100.107.42:27017")


print client['param']['arraysensores'].find()[0]