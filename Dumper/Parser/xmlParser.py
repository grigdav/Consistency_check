# Модуль Парсинга

#Импорт библиотеки для распарсивания
import xml.etree.ElementTree as ET
import os 

class XMLParser:
    def __init__(self, pathToXML):
        self._pathToXML = pathToXML

    def Node_info_Parser(self):
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
        try:
            # main list for ENodeBFunction data
            node_param_name_list = []
            node_param_list=[]
            for elem in self.root.iter(tag ='{EricssonSpecificAttributes.17.28.xsd}vsDataENodeBFunction'):
                # create a list for data from this vsDataENodeBFunction element
                node_param_name = []
                node_param =[]
                # loop over subelements
                for subelem in elem:
                    #print('ENodeBFunction main tag is - %s' %(subelem.tag))
                    # add the subelement tag and text as a tuple
                    node_param_name.append(subelem.tag)
                    node_param.append(subelem.text)
                # add the set of data for this vsDataENodeBFunction element to the main list
                node_param_name_list.append(node_param_name)
                node_param_list.append(node_param)
            print(node_param_name_list[0])
            print(node_param_list[0])
        
        except IOError as error_out :
            print(error_out)        
