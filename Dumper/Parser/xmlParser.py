# Модуль Парсинга

#Импорт библиотеки для распарсивания
import xml.etree.ElementTree as ET
import os 
import csv

class XMLParser:
    def __init__(self, pathToXML):
        self._pathToXML = pathToXML

    def Node_info_Parser(self):
    # Создаем функцию парсинга станций по ID станции.
        files_list = os.path.abspath(self._pathToXML)
        tree = ET.parse(files_list)
        root = tree.getroot()
        try:
            #Записываем вывод в файл
            Write = open('/home/dave/Consistency_check/Dumper/Importer/Import_files/Node_ID.csv', 'w') 
            #Создаем список
            fieldnames = ['Node_id-header' , 'Node_parametrs-header']
            node_id_list =[]
            writer = csv.DictWriter(Write , fieldnames=fieldnames)

            for firstchildren in root.findall('.//{genericNrm.xsd}MeContext'):
                node_id_list.append(firstchildren.attrib)
                # Выводим построчный вывод

            writer.writeheader()
            writer.writerow({ 'Node_id-header' : node_id_list , 'Node_parametrs-header' : 'One world'})
            print('Merge Normal - worked')

            print('Node ID parsed - normal')
        except Exception:
            print('Unable parse XML file - please check Node_info_Parser - function.')
            raise SystemExit

    def CsvMerger(self):
        with open ('/home/dave/Consistency_check/Dumper/Importer/Import_files/Node.csv', 'a') as ENodeBFunction:
            fieldnames = ['Node_id-header' , 'Node_parametrs-header']
            list_1 = ['someItem1', 'someitem2']
            writer = csv.DictWriter(ENodeBFunction , fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({ 'Node_id-header' : list_1 , 'Node_parametrs-header' : 'One world'})
            print('Normal - worked')

    def ENodeBFunction_main_info_parser(self):
        files_list = os.path.abspath(self._pathToXML)
        tree = ET.parse(files_list)
        root = tree.getroot()
        try:
            # Создаем список с данными станци.
            Write = open('/home/dave/Consistency_check/Dumper/Importer/Import_files/ENodeBFunction.csv', 'w', newline='')
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
            Write.write(', \n'.join(str(value) for value in node_param_list))
            Write.close()
            print('ENodeBFunction parameters parsed - normal')
        except IOError as error_out :
            print(error_out)        



