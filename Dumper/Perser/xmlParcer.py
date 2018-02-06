# наброски парсинга


from lxml import etree
    #Импортируем модуль 

def parseExampleXML(xmlFile): 
    with open(xmlFile) as fobj:  
        xml = fobj.read()
        # Функция принимает 1 аргумент: путь к файлу XML.  модуль требует сначала открыть и прочитать пустой файл. (точно не разобрался почему)
    
    root = etree.fromstring(xml)

    book_dict = {} #Перед началом итерации над контекстом,  создадиk объект пустого словаря и пустой список Python. 
    books = []
    for book in root.getchildren():     
        for elem in book.getchildren(): # Находим нужные ветки в древе.
            if not elem.text:  # Если текста в элементе нет, то выведи None.
                text = "None"
            else:
                text = elem.text
            with  open('test.xml', 'w') as data: # Запись текста в файл. (путь - метод)
            	data.write(str(text))
            print(elem.tag + " => " + text) # Вывод текста элементов.
            book_dict[elem.tag] = text
        
        #if book.tag == "book":
           # books.append(book_dict)
            #book_dict = {}
    
    return books

if __name__ == "__main__":
    parseExampleXML(r"books.xml") # путь к файлу парсинга
