# -*- coding: utf-8 -*-
# Модуль Ftp запроса

from ftplib import FTP


from ftplib import FTP

ftp  =  FTP ( 'ftp.cse.buffalo.edu' )      # подключение к хосту по ftb  
ftp . login () 							   # login по умолчанию
#ftp.dir('ubuntu')
data = ftp.retrlines ('LIST')              # Извлечение списка файлов        

print(data)


# Данные о сервере
#ftp = FTP('ftp://10.31.1.132/') # пароль - !!ran.cc \ логин - ran.cc
#ftp.login(user='ran.cc', passwd ='!!ran.cc')
#ftp.connect(HOST, PORT)
#ftp.login(user='ran.cc', passwd ='!!ran.cc')

#data = ftp.retrlines('LIST')
#message = ftp.getwelcome(" OK ")
#print(message())

