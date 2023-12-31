# Встроенная функция `enumerate` в Python часто используется, когда вы хотите итерировать по списку (или другому итерируемому объекту), и вам также нужно получить индекс каждого элемента в этом списке. Функция `enumerate` обычно используется в цикле for.

# Вот общая форма использования функции `enumerate`:

# python
# for index, value in enumerate(some_list):
#     print(f"Индекс: {index}, Значение: {value}")


# В этом коде `index` - это индекс каждого элемента в `some_list`, а `value` - сам элемент.

# Вот простой пример:

# python
fruits = ['яблоко', 'банан', 'манго', 'виноград']

for index, fruit in enumerate(fruits):
    print(f"Фрукт номер {index+1} - это {fruit}")


# Это выведет:


# Фрукт номер 1 - это яблоко
# Фрукт номер 2 - это банан
# Фрукт номер 3 - это манго
# Фрукт номер 4 - это виноград


# По умолчанию `enumerate` начинает считать с `0`. Если вы хотите начать считать с другого числа, вы можете передать функции `enumerate` второй аргумент для указания начала, как здесь:

# python
fruits = ['яблоко', 'банан', 'манго', 'виноград']

for index, fruit in enumerate(fruits, 1):
    print(f"Фрукт номер {index} - это {fruit}")


# Это делает то же самое, что и предыдущий пример, но считает с 1, а не с 0.

# Функция `enumerate` также полезна в сценариях, когда вам нужно отобразить элементы списка на их соответствующие индексы, например, создать словарь с элементами в качестве ключей и индексами как значениями. Это очень удобная функция при работе с итерируемыми объектами в Python.
