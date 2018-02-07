# -*- coding: utf-8 -*-

# Главный модуль, точка запуска.

from Downloader.sftpCaller import copy_file_from_server
from Parser import xmlParser 

def start():
	
	copy_file_from_server()        # Создание вызовов модулей
	#parseXML()


#XML = getter.get()           # Cхема передачи данных - в виде цепочки.
#DS = parser.parse(XML)
#R = storer.store(DS)


if __name__ == '__main__':   # Структура запсука модуля
	start()