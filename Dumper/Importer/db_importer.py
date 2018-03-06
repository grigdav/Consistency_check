
import mysql.connector
from mysql.connector import errorcode

class Importer:
    def __init__(self, dbuser, dbpassword, host, database, charset,): 
        self._dbuser              = dbuser
        self._dbpassword          = dbpassword
        self._host                = host 
        self._database            = database
        self._charset             = charset      

    def Connector(self):
        try:
          cnx = mysql.connector.connect( user       = self._dbuser
                                        ,password   = self._dbpassword
                                        ,host       = self._host
                                        ,database   = self._database
                                        ,use_pure   = False
                                        )
          print('Connect to Data base')
        except mysql.connector.Error as err:
          if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
          elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
          else:
            print(err)
        else:
          cnx.close()
                  

