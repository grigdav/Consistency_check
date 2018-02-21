
import xml.etree.ElementTree as ET
import os 

class rootParser:
    """docstring for rootParser"""
    path_to_file = '/home/dave/XML_files/Ericsson_ful.xml'
    files_list = os.path.abspath(path_to_file)
    tree = ET.parse(files_list)
    root = tree.getroot()

    def Node_info_Parser(self):
        for firstchildren in self.root.findall('.//{genericNrm.xsd}MeContext'):
            Id_info = firstchildren.attrib
            print('%s' %(Id_info))


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

Node_info = rootParser()
Node_info.Node_info_Parser()
#Node_info.ENodeBFunction_main_info_parser()


# ПЕРЕБОР НЕСКОЛЬКИХ XML Файлов
#path_to_file = '/home/dave/XML_files/'

#XML_file = path_to_file + "/XML/"
#files_list = os.listdir(path_to_file)

#all_xml_files =[]
#for file in files_list:
    #all_xml_files.append(ENodeBFunction_main_info_parser(path_to_file + file))

#print('\n'.join(all_xml_files))
