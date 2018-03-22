# -*- coding: utf-8 -*-
import csv

'''def csv_writer(path, fieldnames, data):
    """
    Функция для записи в файл csv
    path - путь до файла
    fieldnames - название столбцов
    data - список из списков
    """
    with open(path, "w", newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# если точка входа наш скрипт
if __name__ == "__main__":
    data = [['lang','name','level', 'something'],
            ['PHP','Ivan','1'],
            ['Python','Vladimir','2'],
            ['Javascript','Egor','3']]

    my_list = []
    fieldnames = data[0]
    cell = data[1:]
    print('столбцы', fieldnames)
    print('ячейки(строки)', cell)
    for values in cell:
        print('строки', values)
        inner_dict = dict(zip(fieldnames, values))
        my_list.append(inner_dict)

    path = "dict_output.csv"
    csv_writer(path, fieldnames, my_list)

l = [[1, 2], [2, 3], [4, 5]]

out = open('dict_output.csv', 'a')
for row in l:
    for column in row:
        out.write('%d;' % column)
    out.write('\n')
out.close()

data = ['5', '18', '0', '0', '0', '0', '2', '0', '0', '0', '0', '0', '0'] # Заполняет в один столбец

with open('dict_output.csv', 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for item in data:
        csv_writer.writerow([item])'''

'''with open('dict_output.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    data = [1,23,76,4, 'f1']
    data2 = [['d2'],['Beans'],[4,'334']]
    writer = csv.DictWriter(csvfile,  fieldnames=fieldnames)

    writer.writeheader()

    for  item2 in  data2:
        writer.writerow({'first_name': data, 'last_name': item2 })'''
import itertools

rows = [1,2,3]
cols =  [['a', 'b'],['c','d'],['e', 'f']]
#flattened = [[cell for cell in row] for row in cols]

#my_dict = [row for row in enumerate( cols, start=0)]
#transposed = [ l for l in (rows, cols)]
#my_dict = [ [row , cols] for row in rows for col in cols]

d1 = [ [ind].append(rows) for ind in enumerate(cols, start=0)]

print(d1)

#print('\n'.join(str(value) for value in flattened))