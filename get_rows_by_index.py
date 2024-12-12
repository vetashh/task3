def fun(name_dic, vals, copy_table=False):
    try:
        dic_res = {}
        list_tab = list(name_dic.values())
        num_row_res = []
        for num_row in range(len(list_tab[0])):
            if list_tab[0][num_row] in vals:
                num_row_res.append(num_row)
        new_row = {key:[name_dic[key][num_row] for num_row in range(len(name_dic[key])) if num_row in num_row_res] for key in name_dic.keys()}
        dic_res.update(new_row)
        if copy_table == True:
            return dic_res
        name_dic.clear()  # Remove all existing items
        name_dic.update(dic_res)
        return name_dic
    except:
        return 'Ошибка! Проверьте корректность введенных данных и попробуйте заново\n'