import csv
import pickle

def fun(name_dic, name_file, file_extension):
    try:
        if file_extension == 'pickle':
            file_res = pickle.dump(name_dic, open(name_file + '.pickle', 'wb'))
        elif file_extension == 'csv':
            file_res = open(name_file, 'w+', encoding='utf-8-sig')
            file_res = csv.writer(file_res, delimiter=';')
            list_res = [list(name_dic.keys())]
            for num_key in range(len(list(name_dic.values())[0])):
                list_res.append([name_dic[key][num_key] for key in name_dic.keys()])
            file_res.writerows(list_res)
        elif file_extension == 'txt':
            file_res = open(name_file, 'w+', encoding='utf-8-sig')
            file_res.write(' '.join([str(el) for el in name_dic.keys()]))
            file_res.write('\n')
            for num_key in range(len(list(name_dic.values())[0])):
                list_res = [name_dic[key][num_key] for key in name_dic.keys()]
                file_res.write(' '.join([str(el) for el in list_res]))
                file_res.write('\n')
        else:
            return 'Ошибка! Проверьте корректность введенных данных и попробуйте заново\n'
        return 'Проверьте создание файла\n'
    except:
        return 'Ошибка! Проверьте корректность введенных данных и попробуйте заново'