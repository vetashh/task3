def fun(name_dic):
    try:
        print(list(name_dic.keys()))
        for row in name_dic.values():
            print(row)
        return ''
    except:
        return 'Ошибка! Проверьте корректность введенных данных и попробуйте заново\n'