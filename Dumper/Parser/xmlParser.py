# наброски парсинга


from lxml import etree, objectify

def parseXML(xmlFile):
    """Функция парсинга"""
    with open(xmlFile) as f:
        xml = f.read()
    
    #tree = etree.Element(xml)
    root = objectify.fromstring(xml)
    
    # возвращаем атрибуты как словарь.
    #attrib = root.attrib

    
    # в цикле выводим всю информацию про элементы (тэги и текст).
    for metaParent in root.getchildren():
        for secondparent in metaParent.getchildren():
            for thirdparent in secondparent.getchildren():
                for firstchildren in thirdparent.getchildren():
                    for secondchildren in firstchildren.getchildren():
                        mainInfo = secondchildren.tag
                        print('MeContext tag is - %s' %(mainInfo))
                        for thirdchildren in secondchildren.getchildren():
                            print(" NodeContext children tag and text is -%s => %s" % (thirdchildren.tag, thirdchildren.text))

    
parseXML('Ericsson.xml')
