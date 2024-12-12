def fun(name_dic, values, column=0):
    list_key = list(name_dic.keys())
    try:
        if type(column) == int:
            if column > 0:
                column = list_key[column-1]
            elif column == 0:
                column = list_key[column]
            else:
                return 'Ошибка! Проверьте корректность введенных данных и попробуйте заново\n'
        for val in values:
            if val != None:
                type_row = type(val)
                break
        for val in name_dic[column]:
            if val != None:
                type_column = type(val)
                break
        if type_column == type_row and len(name_dic[column]) == len(values):
            name_dic[column] = values
            return name_dic
        else:
            return 'Ошибка! Проверьте корректность введенных данных и попробуйте заново\n'
    except:
        return 'Ошибка! Проверьте корректность введенных данных и попробуйте заново\n'