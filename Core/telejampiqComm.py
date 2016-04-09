

from pymongo import MongoClient
class pythonClientDB:

    def __init__(self, server):
        try:
            self.client = MongoClient(server)
        except:
            print "No se pudo conectar"

        self.databasesNames = self.client.database_names()
        self.ID = "0f01s123daj4"

    def readDBS(self):
        return self.databasesNames

    def findDatawithIndex(self, database, collection, data):
        m = 0
        for i in self.client[database][collection].find():
            if data in i.keys():
                return m
            m+=1

    def getDB(self, database, collection):
        vect = []
        dataB = self.client[database]
        coll = dataB[collection].find()

        m = 0
        for i in coll:
            vect.append(i)
            m+=1
        return vect
    def setDB(self,database, collection, data, value):
        indexData = 4
        if data == 'sensor1':
            indexData=0
        elif data == 'sensor2':
            indexData=1

        pastValue = self.getDB(database, collection)[0][data]['value']

        if indexData==0:
            result = self.client[database][collection].update_one(
            {
                "ID":"0f01s123daj4",
                "sensor1":{
                    "value":pastValue,
                    "state":"True",
                    "timeout":0
                },
                "sensor2":{
                    "value":9999,
                    "state":"False",
                    "timeout":0
                }

            },
                {
                    "$set":{

                            "ID":"0f01s123daj4",
                            "sensor1":{
                                "value":value,
                                "state":"True",
                                "timeout":0
                            },
                            "sensor2":{
                                "value":9999,
                                "state":"False",
                                "timeout":0
                            }


                    }
                }

            )
        elif indexData == 1:

            result = self.client[database][collection].update_one(
            {
                "ID":"0f01s123daj4",
                "sensor2":{
                    "value":pastValue,
                    "state":"False",
                    "timeout":0
                },
                "sensor1":{
                    "value":9999,
                    "state":"True",
                    "timeout":0
                }

            },
                {
                    "$set":{

                            "ID":"0f01s123daj4",
                            "sensor2":{
                                "value":value,
                                "state":"False",
                                "timeout":0
                            },
                            "sensor1":{
                                "value":9999,
                                "state":"True",
                                "timeout":0
                            }



                    }
                }

            )




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














