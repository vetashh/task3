def fun(name_dic, row_number):
    try:
        dic1 = {key:name_dic[key][:row_number+1] for key in name_dic.keys()}
        dic2 = {key:name_dic[key][row_number+1:] for key in name_dic.keys()}
        print('Первая таблица:', dic1)
        print('Вторая таблица', dic2)
        return ''
    except:
        return 'Ошибка! Проверьте корректность введенных данных и попробуйте заново\n'