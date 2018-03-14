# -*- coding: utf-8 -*-
# Главный модуль проекта.

# Библиотека для работы с конфигурационным файлом.
import configparser
# Модули для работы
from Downloader import Downloader
from Parser import xmlParser 
from Importer import db_importer

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

    parser = xmlParser.XMLParser(         config['PARSER']['PathToXML']
                                )

    imp_er = db_importer.Importer(        config['IMPORTER']['DbUser']
                                 ,        config['IMPORTER']['DbPassword']
                                 ,        config['IMPORTER']['Host']
                                 ,        config['IMPORTER']['Database']
                                 ,        config['IMPORTER']['Charset']
                                )
    #downloader.download()
    #parser.Node_info_Parser()
    #parser.ENodeBFunction_main_info_parser()
    #parser.CsvMerger()
    imp_er.ConnectChecker()
    imp_er.NodeInfoImporter()

if __name__ == '__main__':
    run()