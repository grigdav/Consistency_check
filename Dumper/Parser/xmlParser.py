# Модуль Парсинга

#Импорт библиотеки для распарсивания
import xml.etree.ElementTree as ET
import os 

class XMLParser:
    def __init__(self, pathToXML):
        self._pathToXML = pathToXML

    def Node_info_Parser(self):
    # Создаем функцию парсинга станций по ID станции.
        files_list = os.path.abspath(self._pathToXML)
        tree = ET.parse(files_list)
        root = tree.getroot()
        try:
            for firstchildren in root.findall('.//{genericNrm.xsd}MeContext'):
                Id_info = firstchildren.attrib
                print('%s' %(Id_info))
        except Exception:
            print('Unable parse XML file - please check Node_info_Parser - function.')
            raise SystemExit

    def ENodeBFunction_main_info_parser(self):
        files_list = os.path.abspath(self._pathToXML)
        tree = ET.parse(files_list)
        root = tree.getroot()
        try:
            # Создаем список с данными станци.
            node_param_list=[]
            for elem in root.iter(tag ='{EricssonSpecificAttributes.17.28.xsd}vsDataENodeBFunction'):
                # создаем список элементов vsDataENodeBFunction.
                node_param =[]
                # спускаемся на уровень ниже
                for subelem in elem:
                    # добавляем полученную информацию в список
                    node_param.append(subelem.text)
                #  и добавляем весь полученный список в главный список vsDataENodeBFunction (так как параметров в этом списке у нас будет много). 
                node_param_list.append(node_param)
            print(node_param_list)
        except IOError as error_out :
            print(error_out)        
