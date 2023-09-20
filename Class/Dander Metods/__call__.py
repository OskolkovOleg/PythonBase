import math

# # класс типа Функтор
# class StringChars:

#     def __init__(self, chars):
#         self.__chars = chars

#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise TypeError('Аргумент должен быть строкой')

#         return args[0].strip(self.__chars)


# s = StringChars('.?/!/.,[]:; ')
# s2 = StringChars(' ')
# res = s(' Hello World! ')
# res2 = s2(' Hello World! ')

# print(res, res2, sep='\n')


# класс декоратор
class Derivate:

    def __init__(self, func):
        self.__fn = func

    # Отраб при вызове Экземпляра класса как функции
    # Вычисление производной
    def __call__(self, x, dx=0.0001, *args, **kwds):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


def df_sin(x):
    return math.sin(x)
print(df_sin(math.pi/3))

# df_sin = Derivate(df_sin)
# print(df_sin(math.pi/3))

# Круче:
@Derivate
def df_sin(x):
    return math.sin(x)
print(df_sin(math.pi/3))