# Модуль Парсинга

#Импорт библиотеки для распарсивания
import xml.etree.ElementTree as ET
import os 
import csv

class XMLParser:
    def __init__(self, pathToXML):
        self._pathToXML = pathToXML


    def ENodeBFunction_main_info_parser(self):

        path = self._pathToXML

        dir_list = [os.path.join(path, x) for x in os.listdir(path)]

        if dir_list:
            # Создадим список из путей к файлам и дат их создания.
            date_list = [[x, os.path.getctime(x)] for x in dir_list]

            # Отсортируем список по дате создания в обратном порядке
            sort_date_list = sorted(date_list, key=lambda x: x[1], reverse=True)

            # Выведем первый элемент списка. Он и будет самым последним по дате
            last_xml_file =(sort_date_list[0][0])

        files_list = os.path.abspath(last_xml_file)
        tree = ET.parse(files_list)
        root = tree.getroot()
        try:
            # Создаем список с данными станци.
            Write = open('/home/dave/Consistency_check/Dumper/Importer/Import_files/ENodeBFunction.csv', 'w', newline='')
            node_param_list=[]
            node_id_list =[]
            matrix = [  node_id_list,
                        node_param_list
                     ]

            for firstchildren in root.findall('.//{genericNrm.xsd}MeContext'):
                current_node_id = firstchildren.attrib
                simplified_node_id = current_node_id.get('id')
                node_id_list.append(simplified_node_id)

            for elem in root.iter(tag ='{EricssonSpecificAttributes.17.28.xsd}vsDataENodeBFunction'):
                # создаем список элементов vsDataENodeBFunction.
                node_param =[]
                # спускаемся на уровень ниже
                for subelem in elem:
                    # добавляем полученную информацию в список
                    node_param.append(subelem.text)
                #  и добавляем весь полученный список в главный список vsDataENodeBFunction (так как параметров в этом списке у нас будет много). 
                node_param_list.append(node_param)

            transposed = []
            for i in range(len(matrix[0])):
                new_row = []
                for row in matrix:
                    new_row.append(row[i])
                transposed.append(new_row)

            Write.write('\n'.join(str(value) for value in transposed))
            Write.close()
            print('ENodeBFunction parameters parsed - normal')
        except IOError as error_out :
            print(error_out)        

    def AdmissionControll_parser(self):
        files_list = os.path.abspath(self._pathToXML)
        tree = ET.parse(files_list)
        root = tree.getroot()
        try:
            # Создаем список с данными станци.
            Write = open('/home/dave/Consistency_check/Dumper/Importer/Import_files/AdmissionControll.csv', 'w', newline='')
            admission_controll_param_list=[]
            node_id_list =[]
            matrix = [  node_id_list,
                        admission_controll_param_list
                        ]

            for firstchildren in root.findall('.//{genericNrm.xsd}MeContext'):
                current_node_id = firstchildren.attrib
                simplified_node_id = current_node_id.get('id')
                node_id_list.append(simplified_node_id)

            for elem in root.iter(tag ='{EricssonSpecificAttributes.17.28.xsd}vsDataAdmissionControl'):
                admission_param =[]
                for subelem in elem:
                    admission_param.append(subelem.text)
                admission_controll_param_list.append(admission_param)

            transposed = []
            for i in range(len(matrix[0])):
                new_row = []
                for row in matrix:
                    new_row.append(row[i])
                transposed.append(new_row)

            Write.write('\n'.join(str(value) for value in transposed))
            Write.close()
            print('DataAdmissionControl parameters parsed - normal')
        except IOError as error_out :
            print(error_out) 