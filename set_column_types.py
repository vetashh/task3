def fun(name_dic, type_row, by_number = True):
    dic_res = {}
    try:
        for num_key, key in enumerate(name_dic.keys()):
            try:
                name_dic[key] = list(map(type_row, name_dic[key]))
                if by_number:
                    new_row = {num_key: type_row}
                else:
                    new_row = {key: type_row}
            except:
                if by_number:
                    new_row = {num_key: f'не удалось поменять тип на {type_row}'}
                else:
                    new_row = {key: f'не удалось поменять тип на {type_row}'}
            dic_res.update(new_row)
        return dic_res
    except:
        return 'Ошибка! Проверьте корректность введенных данных и попробуйте заново\n'