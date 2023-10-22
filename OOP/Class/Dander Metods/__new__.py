# __new__() вызывается до создания объекта
# __init__() вызывается после создания объекта

# cls ссылается на сам класс а self на экземпляр

# class Man():
#     __instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)

#         return cls.__instance

#     def __init__(self):
#         print('YES')

#     def __del__(self):
#         Man.__instance = None

#     def close(self):
#         print('Закрытие')


# a = Man()
# a1 = Man()


class Point:
    def __new__(cls, *args, **kwargs): # Point(1, 2) аргументы автоматически предаются в __new__() а потом идут в __init__()
        print(f"Вызов __new__ для  {cls}")
        return super().__new__(cls) # Все классы авто наслед от object

    def __init__(self, x=0, y=0) -> None:
        print(f"Вызов __init__ для  {self}")
        self.x = x
        self.y = y


pt = Point(1, 2) # Экземпляр класса не создался Т.к __new__ должен вернуть адрес объекта
print(pt)


class Example(tuple):
    def __new__(cls, urls):
        urls_tuple = tuple(f"https://{url}" for url in urls)
        return super().__new__(cls, urls_tuple)

    # def __init__(self, urls):
    #     print(self)
    
a = Example(["domain.com", "example.com"])
print(f"{a=}")