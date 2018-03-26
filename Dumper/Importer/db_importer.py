import os
import sys
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
        config = configparser.ConfigParser()
        config.read('Dumper/Configs/dumper.ini')
        cursor = cnt.cursor()
        try:
          info = {  'EnodeBfile'  :  config['DATABASE']['ENodeBFile']
                  , 'EnodeBtable' :  config['DATABASE']['ENodeBTable']
                  , 'Admissfile'  :  config['DATABASE']['AdmissFile']
                  , 'Admisstable' :  config['DATABASE']['AdmissTable']
          }
          EnodeB =  ''' LOAD DATA LOCAL INFILE '%(EnodeBfile)s' 
                        INTO TABLE %(EnodeBtable)s 
                        FIELDS TERMINATED BY ', '
                    '''
          AdmissionControll = ''' LOAD DATA LOCAL INFILE '%(Admissfile)s' 
                                  INTO TABLE %(Admisstable)s 
                                  FIELDS TERMINATED BY ', '

                              '''
          EnodeBquery = EnodeB % info
          Admissquery = AdmissionControll % info

          cursor.execute(EnodeBquery)
          cursor.execute(Admissquery)
          cnt.commit()
          print('Successful import to Data base')
        except Exception:
            print('You have a problem with Import - please check NodeInfoImporter')
            raise SystemExit 
        finally:
          cnt.close()
