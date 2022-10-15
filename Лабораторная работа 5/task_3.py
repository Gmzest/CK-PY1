import random
def get_unique_list_numbers() -> list[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел
    lst_ = []
    step = 0
    while step != 15:
        check = random.randint(-10, 10)
        if check not in lst_:
            lst_.append(check)
            step += 1
    return lst_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
