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
            #Записываем вывод в файл
        Write = open('/home/dave/Consistency_check/Dumper/Importer/Import_files/Node_ID.csv', 'w') 
            #Создаем список
        fieldnames = ['Node_id-header' , 'Node_parametrs-header']
        node_id_list =[]
        writer = csv.DictWriter(Write , fieldnames=fieldnames)

        for firstchildren in root.findall('.//{genericNrm.xsd}MeContext'):
            current_node_id = firstchildren.attrib
            simplified_node_id = current_node_id.get('id')
            node_id_list.append(simplified_node_id)
        
        # Выводим построчный вывод
        Write.write('\n'.join(str(value) for value in node_id_list))
        Write.close()

        print('Node ID parsed - normal')

    '''def CsvMerger(self):
        csvWithNodeIds = open ('/home/dave/Consistency_check/Dumper/Importer/Import_files/Node_ID.csv', 'r', newline='')        
        csvWithENodeBFunctions = open ('/home/dave/Consistency_check/Dumper/Importer/Import_files/ENodeBFunction.csv', 'r', newline='')

        nodeIds = csv.reader(csvWithNodeIds)
        eNodeBFunctions = csv.reader(csvWithENodeBFunctions)

        # Мы точно знаем что количество строк в nodeIds совпадает с количеством строк в eNodeBFunctions
        listForNodeIds = []
        listForENodeBFunctions = []

        # Превращаем первый дикт из первого CSV в список айдишников
         for rowIndex1, nodeIdRow in enumerate(nodeIds, start=0):   # default is zero
            for key1, nodeId in nodeIdRow.iteritems():
                listForNodeIds.append([nodeId])
        
        # Превращем второй дикт из второго CSV в список пар ключ-значение
        # где ключ - имя столбца а значение - это значение в данном столбце в этой строке
        # Получаем список списков
        for rowIndex2, eNodeBFunctionsRow in enumerate(eNodeBFunctions, start=0):   # default is zero
            l = []
            for key2, eNodeBFun in eNodeBFunctionsRow.iteritems():
                l.append((key2, eNodeBFun))
            listForENodeBFunctions.append(l)

        # Бежим по второму списку списков чтобы добавить айдишники в начало соответствующего списка-элемента
        # в итоге получаем список списков с полными данными
        for ind, listForOneRow in enumerate(listForENodeBFunctions, start=0):   # default is zero
            listForOneRow.insert(0, ('Node_id-header', listForNodeIds[ind]))

        # превращаем тот список списков в дикт
        ourFinalDict = listForENodeBFunctions to dict
        writeThirdCSVFrom ourFinalDict '''        

    def ENodeBFunction_main_info_parser(self):
        files_list = os.path.abspath(self._pathToXML)
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
            for elem in root.iter(tag ='{EricssonSpecificAttributes.17.28.xsd}vsDataAdmissionControl'):
                # создаем список элементов vsDataENodeBFunction.
                admission_param =[]
                # спускаемся на уровень ниже
                for subelem in elem:
                    # добавляем полученную информацию в список
                    admission_param.append(subelem.text)
                #  и добавляем весь полученный список в главный список  (так как параметров в этом списке у нас будет много). 
                admission_controll_param_list.append(admission_param)
            Write.write('\n'.join(str(value) for value in admission_controll_param_list))
            Write.close()
            print('DataAdmissionControl parameters parsed - normal')
        except IOError as error_out :
            print(error_out) 