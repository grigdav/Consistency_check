# Consistency Check

Приложения для контроля параметров станций 4G,3G и 

## Настройка окружения

### Python

В первую очередь, убедитесь в том, что у вас установлены программы `python3` и `pip3`. Если они отсутствуют, установите их:
 
```
$ sudo apt install python3-pip3
```

Проверьте версии:

```
$ python3 --version
Python 3.5.2
$ pip3 --version
pip 8.1.1 from /usr/lib/python3/dist-packages (python 3.5)
```

Версия `pip3` может быть более новой, это хорошо.

## Обзор структуры проекта

*`Configs` - папка с конфигами проекта.
*`Downloader` -  в этой папке находится модуль для скачивания XML файла с сервера OSS.
    *`__init__` - стандартный пакет python для организации модулей.
    *`Downloader.py` - собственно, сам файл с модулем.
*`Importer` - каталог с модулем записи полученных данных в DB.
*`Parser` - каталог с модулем парсинга и файлом XML(для работы - в дальнейшем он будет подвержен удалению).
    *`xmlParser.py` - файл с модулем парса.
    *`Ericsson.xml` - пример XML файла - с которым нужно работать ( файл содержит информацию всего 1 станции).
*`main.py` - модуль точки входа.