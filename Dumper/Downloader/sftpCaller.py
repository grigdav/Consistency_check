# -*- coding: utf-8 -*-
# Модуль Ftp запроса

import pysftp

def copy_file_to_server():     
		# Создаем функцию копирования файлов с сервера по sftp запросу
	cnopts = pysftp.CnOpts()
	cnopts.hostkeys.load('.ssh/known_hosts')    
		# Проверка ключ хоста. Так как сервера находятся в одной локальной сети, то и проверка ключа = None.

	with pysftp.Connection(host='10.31.1.132', username='ran.cc', password='!!ran.cc', cnopts=cnopts) as sftp:                      
		# Создание подключения к серверу

		Get_file = sftp.get_d('/var/opt/ericsson/nms_umts_wran_bcg/files/export/cc', '/home/dave/XML_files', preserve_mtime=True)
			#Копирование файлов. Местоназначение файлов на сервере, путь копирования на локальный сервер, проверка по времени.

		sftp.close()
			# Закрытие сессии
		

copy_file_to_server()

