def fun(name_dic1, name_dic2):
    try:
        dic_res = {}
        for key in name_dic2.keys():
            if key not in name_dic1.keys():
                new_col = {key:[None for _ in range(len(list(name_dic1.values())[0]))]}
                name_dic1.update(new_col)
        list_dic2 = list(name_dic2.values())
        for num_row in range(len(list_dic2[0])):
            row = {key:name_dic2[key][num_row] for key in name_dic2}
            for key in name_dic1.keys():
                if key in row and row[key] != None:
                    name_dic1[key].append(row[key])
                else:
                    name_dic1[key] += [None]
        dic_res.update(name_dic1)
        return dic_res
    except:
        return 'Ошибка! Проверьте корректность введенных данных и попробуйте заново\n'