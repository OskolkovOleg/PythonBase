# Декораторы функций
from time import time


def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("--- что-то делаем перед вызовом функции ---")
        res = func(*args, **kwargs)
        print("--- что-то делаем после вызова функции ---")
        return res
    return wrapper


@func_decorator
def some_func(title, tag):
    print(" Вызов функции some_func", title, tag)
    return 0


print(some_func("sd", 'asd'))


def test_time(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        res = func(*args, **kwargs)
        print(f"Время работы функции: {time()-start_time}")
        return res
    return wrapper


# Медленный алгоритм Евклид
@test_time
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


# Быстрый алгоритм Евклид
@test_time
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


get_fast_nod(2, 21_000_000_0)
get_nod(2, 21_000_000_0)


# def func_decorator(func):
#     def wrapper():
#         print("--- что-то делаем перед вызовом функции ---")
#         func()
#         print("--- что-то делаем после вызова функции ---")
#     return wrapper


# def some_func():
#     print(" Вызов функции some_func")


# f = func_decorator(some_func)
# f()
# some_func = func_decorator(some_func)
# some_func()


# @func_decorator
# def some_func():
#     print(" Вызов функции some_func")


# some_func()


# def func_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("--- что-то делаем перед вызовом функции ---")
#         func(*args, **kwargs)
#         print("--- что-то делаем после вызова функции ---")
#     return wrapper


# @func_decorator
# def some_func(title, tag):
#     print(" Вызов функции some_func",title, tag)


# some_func("sd",'asd')

# # def decorate(funct):
# #     def wrapper():
# #         print("wraper")
# #         funct()
# #     return wrapper


# # @decorate
# # def test():
# #     print("test")

# # test()


# # def decorate(funct):
# #     def wrapper(value):
# #         print("wraper")
# #         funct(value)
# #     return wrapper


# # @decorate
# # def test(value):
# #     print(f"test, {value=}")

# # test("12")
