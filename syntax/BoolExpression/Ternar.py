# <expression on True> if <predicate> else <expression on False>

import random


def abs(number):
    if number >= 0:
        return number
    return -number


def abs(number):
    return number if number >= 0 else -number


# Так делать не стоит:
1 if 1 > 2 and 1 > 3 else 2 if 2 > 3 else 3

1 if 1 == (1 if 1 == 1 else 2) else 2

#
condition = True
print(2 if condition else 1/0)  # Подводный камень

# Прикольно НО могут создать ошибки
status = True
connect_label = ("1.0", "2.0")[status]
print(f"Server version: {connect_label}")


num1 = random.random()
num2 = random.random()
print((num1, num2)[num1 > num2])


# Тоже плохой пример: крч гн код
print(True or "Some")
print(False or "Some")

func_output = None
msg = func_output or "Не было возвращено данных"
print(msg)
