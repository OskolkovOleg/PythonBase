# Не рекомендуется использовать особенно ,=

from random import randint

a = [2,5,4,56]
b,*_ = a
print(b)


def get_values() -> list:
    return [randint(0, 9) for _ in range(20)]


user_id, user_photo, user_message, *values = get_values()
print(user_id)
print(user_photo)
print(user_message)
print(values)
