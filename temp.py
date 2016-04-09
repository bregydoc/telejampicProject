
import Core.telejampiqComm as comm
'''
client = MongoClient("mongodb://10.100.107.125:27017")
databases = client.database_names()

base = client['telejampiqDB']

coll = base['sensores'].find()

for i in coll:
    print i
'''
'''
dataBase = comm.pythonClientDB("mongodb://10.100.107.125:27017")

dataBase.setDB('telejampiqDB','sensores','sensor1',1111)
dataBase.setDB('telejampiqDB','sensores','sensor2',2222)

print dataBase.getDB('telejampiqDB','sensores')
'''

dataBase = comm.pythonClientDB("mongodb://10.100.107.42:27017")

print dataBase.getDB('param', 'arraysensores')

dataBase.setDB('param','arraysensores','sensor2',4360)

print dataBase.getDB('param', 'arraysensores')



