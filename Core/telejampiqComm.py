

from pymongo import MongoClient
class pythonClientDB:

    def __init__(self, server):
        try:
            self.client = MongoClient(server)
        except:
            print "No se pudo conectar"

        self.databasesNames = self.client.database_names()

    def readDBS(self):
        return self.databasesNames

    def getDB(self, database, collection):
        vect = []
        dataB = self.client[database]
        coll = dataB[collection].find()

        m = 0
        for i in coll:
            vect.append(i)
            m+=1
        return vect

