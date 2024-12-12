def fun(name_dic, by_number = True):
    try:
        types = {}
        if by_number:
            for num_key, key in enumerate(name_dic.keys()):
                for val in name_dic[key]:
                    if val != None:
                        type_row = {num_key:type(val)}
                        types.update(type_row)
                        break
        else:
            for key in name_dic.keys():
                for val in name_dic[key]:
                    if val != None:
                        type_row = {key: type(val)}
                        types.update(type_row)
                        break
        return types
    except:
        return 'Ошибка! Проверьте корректность введенных данных и попробуйте заново\n'