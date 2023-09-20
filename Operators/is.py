# a = 5
# b = 5
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))
a = 11111111
b = 11111111 # Даже так id не всегда одинаковые
# print(id(a))
# print(id(b))
# print(a is b)

# от -5 до 256 значения имеют одинак id,
#  а далее под каждую переменную отдельня ячейка, 
# но так только для терминала

# a = "hello"
# b = "hello"
# print(a is b)

# a = "hello"
# b = "hell"
# b += "o"
# print(a is b)

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a is b)

# a = [1, 2, 3]
# b = a          # Плохо так делать!!!
# print(a is b)

# a = [1, 2, 3]
# b = a.copy()  # АААААААААААААААААА
# print(a is b)

"""Нужно использовать"""
a = None
print(a is None)

a = True
print(a is True)

a = False
print(a is False)

