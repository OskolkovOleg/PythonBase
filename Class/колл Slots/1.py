# __slots__
import timeit

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


class Point2D:
    # Предопределение локальных свойств только они __dict__ отсутствует
    # Усменьшает объем занимаемой памяти
    # Ускоряет работу
    __slots__ = ("x", "y")
    MAX_COORD = 100

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


pt = Point(1, 2)
p = Point2D(1, 2)
p.x = 23
del p.x
p.x = 243

print(pt.__sizeof__() + pt.__dict__.__sizeof__())
print(p.__sizeof__())


print(timeit.timeit(pt.calc))
print(timeit.timeit(p.calc))
