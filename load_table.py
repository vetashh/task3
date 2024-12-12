import csv
import pickle

def fun(file_link):
    try:
        if file_link.endswith('.pickle'):
            file_link = open(file_link, 'rb')
            table = pickle.load(file_link)
        elif file_link.endswith('.csv'):
            table = {}
            file = open(file_link, 'r', encoding='utf-8-sig')
            reader = csv.reader(file)
            for num_row, row in enumerate(reader):
                row = row[0].split(';')
                if not num_row:
                    row_1 = row
                    dic = [[] for _ in range(len(row))]
                else:
                    for num_el in range(len(row)):
                        dic[num_el].append(row[num_el])
            table = {name_col:dic[num] for num, name_col in enumerate(row_1)}

        for key in table:
            for num in range(len(table[key])):
                table[key][num] = None if table[key][num] in ['', 'None'] else table[key][num]
        return table
    except:
        return 'Ошибка! Проверьте корректность введенных данных и попробуйте заново\n'