# # Может иметь лишь один экземпляр

# class DataBase:
#     __instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)

#         return cls.__instance  # Вот и весь прикол

#     def __del__(self):
#         DataBase.__instance = None

#     def __init__(self, user, psw, port):
#         self.user = user
#         self.psw = psw
#         self.port = port

#     def connect(self):
#         print(
#             f"Соединение с БД: {self.user}, {self.psw}, {self.port}")

#     def close(self):
#         print("Закрытие соедиения с БД")

#     def read(self):
#         return "Данные из БД"

#     def write(self, data):
#         print(f"Запись в БД {data}")


# db = DataBase("root", "1234", 80)
# # Поменяли свойства Это нненадо так
# db2 = DataBase("root2", "56789", 40)
# print(id(db), id(db2))


# #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# class Singleton(type):
#     _instance = {}

#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instance:
#             cls._instance[cls] = super(
#                 Singleton, cls).__call__(*args, **kwargs)
#         return cls._instance[cls]


# class Logger(metaclass=Singleton):
#     pass


# a = Logger()
# b = Logger()
# print(a)
# print(b)


# class Logger():
#     pass


# a = Logger()
# b = Logger()
# print(a)
# print(b)


class Singleton():
    _instance = {}
    
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(
                Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance[cls]


class Logger(Singleton):
    pass


a = Logger()
b = Logger()
print(a)
print(b)
