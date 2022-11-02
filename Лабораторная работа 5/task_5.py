import random
import string

def get_random_password(n = 8) -> str:
    ...  # TODO написать функцию генерации случайных паролей
    return random.sample([f"{i}" for i in string.digits] +
                         [f"{i}" for i in string.ascii_uppercase] +
                         [f"{i}" for i in string.ascii_lowercase], k = n)

print("".join(get_random_password()))
