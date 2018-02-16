import xml.etree.ElementTree as ET
import os 

def ENodeBFunction_main_info_parser():

    try:
        path_to_file = '/home/dave/XML_files/Ericsson.xml'
        files_list = os.path.abspath(path_to_file)
        tree = ET.parse(files_list)
        root = tree.getroot()
        ns = {'second_info':'EricssonSpecificAttributes.17.28.xsd',
            'main_info':"genericNrm.xsd"}

        # main list for ENodeBFunction data
        alarmTime_list = []
        for elem in root.iter(tag ='{EricssonSpecificAttributes.17.28.xsd}vsDataENodeBFunction'):
            # create a list for data from this alarmTime element
            data = []
            # loop over subelements
            for subelem in elem:
                #print('ENodeBFunction main tag is - %s' %(subelem.tag))
                # add the subelement tag and text as a tuple
                data.append((subelem.text))
            # add the set of data for this alarmTime element to the main list
            alarmTime_list.append(data)
        return(alarmTime_list[0][1:7])
    
    except IOError as e :
        print(e)
print(ENodeBFunction_main_info_parser())

#path_to_file = '/home/dave/XML_files/'

#XML_file = path_to_file + "/XML/"
#files_list = os.listdir(path_to_file)

#all_xml_files =[]
#for file in files_list:
    #all_xml_files.append(ENodeBFunction_main_info_parser(path_to_file + file))

#print('\n'.join(all_xml_files))

def EnodeBFunction_id_parser():
    path_to_file = '/home/dave/XML_files/Ericsson.xml'
    files_list = os.path.abspath(path_to_file)
    tree = ET.parse(files_list)
    root = tree.getroot()
    for firstchildren in root.findall('.//{genericNrm.xsd}MeContext'):
        Id_info = firstchildren.attrib
        print(Id_info)
EnodeBFunction_id_parser()
