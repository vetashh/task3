def fun(name_dic, column=0):
    list_key = list(name_dic.keys())
    try:
        if type(column) == int:
            if column > 0:
                column = list_key[column-1]
            elif column == 0:
                column = list_key[column]
            else:
                return 'Ошибка! Проверьте корректность введенных данных и попробуйте заново\n'
        return name_dic[column]
    except:
        return 'Ошибка! Проверьте корректность введенных данных и попробуйте заново\n'