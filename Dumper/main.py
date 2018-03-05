# -*- coding: utf-8 -*-
# Главный модуль проекта.

# Библиотека для работы с конфигурационным файлом.
import configparser
# Модули для работы
from Downloader import Downloader
from Parser import xmlParser 

def run():
    # Читаем конфигурационный файл (проверяя возможные проблемы)
    try:
        config = configparser.ConfigParser()
        config.read('Configs/dumper.ini')              # Подразумевается, что путь к конфигу читается из аргумента командной строки.
    except Exception:
        print('Cannot read configuration file, fault!')
        raise SystemExit

    downloader = Downloader.Downloader(   config['DOWNLOADER']['IPv4']
                                        , config['DOWNLOADER']['Login']
                                        , config['DOWNLOADER']['Password']
                                        , config['DOWNLOADER']['PathToSshKey']
                                        , config['DOWNLOADER']['PathToRemoteXML']
                                        , config['DOWNLOADER']['SaveTo']
                                      )

    parser = xmlParser.XMLParser(  config['PARSER']['PathToXML']
                                )
    #downloader.download()
    parser.Node_info_Parser()
    # К этому моменту XML с сервера уже скачан и уже лежит по пути SaveTo.

    # parseXML()

if __name__ == '__main__':
    run()