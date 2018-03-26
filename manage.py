# -*- coding: utf-8 -*-

#!/usr/bin/env python3

# Модули для работы
import os
import sys
from Dumper.Downloader import Downloader
from Dumper.Parser import xmlParser 
from Dumper.Importer import db_importer

# Библиотека для работы с конфигурационным файлом.
import configparser

def run():
    # Читаем конфигурационный файл (проверяя возможные проблемы)
    try:
        config = configparser.ConfigParser()
        # Подразумевается, что путь к конфигу читается из аргумента командной строки.
        config.read('Dumper/Configs/dumper.ini')              
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
    parser.ENodeBFunction_main_info_parser()
    #parser.AdmissionControll_parser()
    imp_er.ConnectChecker()
    imp_er.NodeInfoImporter()

if __name__ == "__main__":

    run()
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Consistency_check.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)



