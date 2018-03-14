
import mysql.connector
from mysql.connector import errorcode
import configparser


class Importer:
    def __init__(self, dbuser, dbpassword, host, database, charset): 
        self._dbuser              = dbuser
        self._dbpassword          = dbpassword
        self._host                = host 
        self._database            = database
        self._charset             = charset      

    def ConnectChecker(self):
        try:
          cnt = mysql.connector.connect( user       = self._dbuser
                                        ,password   = self._dbpassword
                                        ,host       = self._host
                                        ,database   = self._database
                                        ,use_pure   = False
                                        )
          print('Successful connect to Data base')
          return(cnt)
        except mysql.connector.Error as err:
          if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
          elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
          else:
            print(err)
        finally:
          cnt.close()

    def NodeInfoImporter(self):
        cnt = mysql.connector.connect( user       = self._dbuser
                                      ,password   = self._dbpassword
                                      ,host       = self._host
                                      ,database   = self._database
                                      ,use_pure   = False
                                      )
        cursor = cnt.cursor()
        try:
          info = {  'file' : '/home/dave/Consistency_check/Dumper/Importer/Import_files/Node_ID.csv'
                  , 'table' : 'Dumper_enodebfunction'
                  , 'except' : 'field_enodeb_stnNodes'
          }
          dm = '''LOAD DATA LOCAL INFILE '%(file)s' 
                  INTO TABLE %(table)s 
                '''
          query = dm % info 
          cursor.execute(query)
          cnt.commit()
          print('Successful import to Data base')
        except Exception:
            print('You have a problem with Import - please check NodeInfoImporter')
            raise SystemExit 
        finally:
          cnt.close()