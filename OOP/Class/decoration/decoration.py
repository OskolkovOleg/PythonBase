class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    # Работает только с атрибутами всего класса cls
    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and Vector.validate(y):  # ЛУЧШЕ self.validate(x)
            self.x = x
            self.y = y

        print(self.norm2(5, 6))

    def get_coord(self):
        return self.x, self.y

    @staticmethod  # Не имеют доступа не к self не к cls
    def norm2(x, y):
        return x*x + y*y


v = Vector(1, 2)
print(Vector.validate(5))
print(Vector.norm2(5, 6))
res = Vector.get_coord(v)
print(res)
pt = Vector(1, 2)
# pt.set_coord('1', 2)
print(pt.get_coord())
