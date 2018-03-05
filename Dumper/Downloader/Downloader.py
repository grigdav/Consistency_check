
# -*- coding: utf-8 -*-
# Модуль загрузки XML-файла с удалённого сервера.

# Библиотека для использования протокола SFTP.
import pysftp

class Downloader:
    def __init__(self, ipv4, login, password, pathToSshKey, pathToRemoteXML, saveXmlTo):
        self._ipv4             = ipv4
        self._login            = login
        self._password         = password
        self._pathToSshkey     = pathToSshKey
        self._pathToRemoteXML  = pathToRemoteXML
        self._saveXmlTo        = saveXmlTo

    def download(self):
    # Создаем функцию копирования файлов с сервера по sftp запросу
        cnopts = pysftp.CnOpts()
        try:
            # Проверка ключ хоста. Так как сервера находятся в одной локальной сети, то и проверка ключа = None.
            cnopts.hostkeys.load(self._pathToSshkey)
            # Создание подключения к серверу
            with pysftp.Connection( host     = self._ipv4,
                                    username = self._login,
                                    password = self._password,
                                    cnopts   = cnopts) as sftp:
                #Копирование файлов.
                sftp.get_d(self._pathToRemoteXML,
                            self._saveXmlTo,
                            preserve_mtime = True) # Проверка соединения по времени.
                # Закрытие SFTP-сессии.
                sftp.close()
        except Exception:
            print('Unable to download XML-file from remote server.')
            raise SystemExit

        print('Download: done!')