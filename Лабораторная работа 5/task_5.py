import random
import string

def get_random_password(n = 8) -> str:
    ...  # TODO написать функцию генерации случайных паролей
    return random.sample([i for i in string.digits] +
                         [i for i in string.ascii_uppercase] +
                         [i for i in string.ascii_lowercase], k = n)

print(get_random_password())
