# print(type(int))


# class A:
#     ...


# print(type(A))


# class Point:
#     MAX_COORD = 100
#     MIN_COORD = 0


# Эквилиентно:
# A = type("Point", (), {"MAX_COORD": 100, "MIN_COORD": 0})
# pt = A
# print(pt.MAX_COORD)


# class B1: pass
# class B2: pass

# A = type("Point", (B1, B2), {"MAX_COORD": 100, "MIN_COORD": 0})
# print(A.__mro__)


# Добавление методов
# def method1(self):
#     print(self.__dict__)

# A = type("Point", (), {"MAX_COORD": 100, "method1": method1})

# a = A()
# a.method1()

# A = type("Point", (), {"MAX_COORD": 100, "method1": lambda self: self.MAX_COORD})

# a = A()
# print(a.method1())

