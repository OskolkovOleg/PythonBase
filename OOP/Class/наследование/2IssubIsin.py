class Geom:
    pass


class Line(Geom):
    pass


print(Geom.__name__)
g = Geom()
print('Вывод из str класса Object', g)


# Является ли класс подклассом
print(issubclass(Line, Geom))
print(issubclass(Geom, Line))
print(issubclass(int, object))

print(isinstance(g, Geom))
print(isinstance(g, object))
print(isinstance(Geom, object))


class Vector(list):
    def __str__(self) -> str:
        return "!!".join(map(str, self))

v = Vector([1, 2, 3])
print(v)