def fun(name_dic,value,column=0):
    list_key = list(name_dic.keys())
    try:
        if type(column) == int:
            if column > 0:
                column = list_key[column-1]
            elif column == 0:
                column = list_key[column]
            else:
                return 'Ошибка! Проверьте корректность введенных данных и попробуйте заново\n'
        if type(name_dic[column][0]) == type(value):
            name_dic[column][0] = value
            return name_dic
        else:
            return 'Ошибка! Проверьте корректность введенных данных и попробуйте заново\n'
    except:
        return 'Ошибка! Проверьте корректность введенных данных и попробуйте заново\n'