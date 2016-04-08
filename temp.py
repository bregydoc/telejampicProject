
import Core.telejampiqComm as comm
'''
client = MongoClient("mongodb://10.100.107.125:27017")
databases = client.database_names()

base = client['telejampiqDB']

coll = base['sensores'].find()

for i in coll:
    print i
'''

dataBase = comm.pythonClientDB("mongodb://10.100.107.125:27017")

print dataBase.getDB('telejampiqDB','sensores')

dataBase.setDB('telejampiqFB','sensores','sensor1',1234)




tjq = comm.telejampiqData("mongodb://10.100.107.125:27017")

print tjq.downloadData()

