def fun(name_dic, start=1, stop=None, copy_table=False):
    try:
        if not stop:
            stop = len(name_dic.keys())
        dic_res = {key:name_dic[key][start:stop+1] for key in name_dic.keys()}
        if copy_table == True:
            return dic_res
        name_dic.clear()  # Remove all existing items
        name_dic.update(dic_res)
        return name_dic
    except:
        return 'Ошибка! Проверьте корректность введенных данных и попробуйте заново\n'