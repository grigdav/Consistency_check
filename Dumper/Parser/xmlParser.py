# наброски парсинга


#from lxml import etree, objectify

import xml.etree.ElementTree as ET

def node_Id_parser(xmlFile):
    """Функция парсинга ID станции"""
    with open('Ericsson.xml' , 'rt') as f:
        #xml = f.read()
    
     tree = ET.parse(xmlFile)
    
     root = tree.getroot()
    
    # возвращаем атрибуты как словарь.
    #attrib = root.attrib

    
        # в цикле выводим  информацию аттрибута root-а, - она будет ID строки в DB, так как содержит ID станции.
    for metaParent in root.getchildren():
        for secondparent in metaParent.getchildren():
            for thirdparent in secondparent.getchildren():
                for firstchildren in thirdparent.findall('.//{genericNrm.xsd}MeContext'):
                    Id_info = firstchildren.attrib
                    print(Id_info)


    
node_Id_parser('Ericsson.xml')


def node_Main_info_parser(xmlFile):  # Функция вывода main параметров Node 
    with open('Ericsson.xml' , 'rt') as f:
    
    
     tree = ET.parse(xmlFile)
    
     root = tree.getroot()

    for metaParent in root.getchildren():
        for secondparent in metaParent.getchildren():
            for thirdparent in secondparent.getchildren():
                for firstchildren in thirdparent.findall('.//'):
                    Node_tag = firstchildren.tag
                    Node_text = firstchildren.text
                    #print(Node_tag)
                    if Node_tag >= '{genericNrm.xsd} ':
                        print('Node main tag is - %s , \n Node main param is -%s' % (Node_tag, Node_text))
                    else: 
                        print ('Other param')
                   
   

node_Main_info_parser('Ericsson.xml')
