from LoadSave import load_table
table = load_table.fun('table.csv')
print(table, '\n')

from LoadSave import save_table
print(save_table.fun(table, 'table_res', 'txt'))

from functions import get_rows_by_number
print(get_rows_by_number.fun(table, 1, 2, True))
print(table, '\n')

from functions import get_rows_by_index
print(get_rows_by_index.fun(table, ['Анна', 'Дмитрий'], True))
print(table, '\n')

from functions import get_column_types
print(get_column_types.fun(table, True), '\n')

from functions import set_column_types
print(set_column_types.fun(table, int), '\n')

from functions import get_values
print(get_values.fun(table))
print(get_values.fun(table, 'Город проживания'), '\n')

table2 = save_table.fun(get_rows_by_number.fun(table, 1, 1, True), 'table 2', 'pickle')
table2 = load_table.fun('table 2.pickle')
print(table2, '\n')

from functions import get_value
print(get_value.fun(table2, column=3), '\n')

from functions import set_value
print(set_value.fun(table2,'Синий',column=2), '\n')

from functions import set_values
print(set_values.fun(table, ['Мария', 'Григорий', 'Светлана', 'Маруся']))

from functions import print_table
print(print_table.fun(table))

from functions import concat
print(concat.fun(table, table2))

table3 = {'Имя сотрудника': ['Вера'], 'Денег на счету': [10000], 'Город проживания': ['Владимир']}
print(concat.fun(table, table3), '\n')

from functions import split
print(split.fun(table, 2))