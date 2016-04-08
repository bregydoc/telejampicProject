

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
    def setDB(self,database,collection,data,value):
        result = self.client[database][collection].update_one(
            {data: 9999.0},
            {
                "$set":{
                    data: value
                }
            }
        )
        print result


class telejampiqData:

    def __init__(self, server):
        self.comm = pythonClientDB(server)

    def structParse(self, vectorDeDatos):
        longitud = len(vectorDeDatos)
        if longitud==4:
            logFinal = '{"sensor1":'+str(vectorDeDatos[0])+","+'"sensor2":'+str(vectorDeDatos[1])+","+'"sensor3":'+ str(vectorDeDatos[2])+'}'
        else:
            print "Vector de datos incorrecto"


    def refreshData(self):
        pass

    def uploadData(self):
        pass



    def downloadData(self):

        vectF = []
        data = self.comm.getDB('telejampiqDB','sensores')
        for i in range(0,len(data)):
            vectF.append(data[i]['sensor{0}'.format(i+1)])

        return vectF














