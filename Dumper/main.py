# -*- coding: utf-8 -*-

# Главный модуль, точка запуска.

from Downloader.sftpCaller import copy_file_from_server

def start():
	
	getter = copy_file_from_server()        # Создание вызовов модулей
	#parser = newParser()
	#storer = newStorer()


#XML = getter.get()           # Cхема передачи данных - в виде цепочки.
#DS = parser.parse(XML)
#R = storer.store(DS)


if __name__ == '__main__':   # Структура запсука модуля
	start()