def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = "".join(str_.lower().split())
    key_dict = {}
    for i in str_:
        if i.isalpha():
            if i not in key_dict:
                key_dict[i] = 1
            else:
                key_dict[i] += 1
    return key_dict


    ###### Вторая функция ######


def dict_stat(dictionary):
    temp = 0
    new_dict = {}
    for key in dictionary:
        temp += dictionary[key]
    for key in dictionary:
        new_dict[key] = (dictionary[key] / temp) * 100
    return new_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
