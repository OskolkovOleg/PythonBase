class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        self.x = x
        self.y = y


    # Вызывается автоматически, при получении свойства c именем item (self, item)
    def __getattribute__(self, __name):
        print("__getattribute__")
        if __name == 'x':
            raise ValueError("Доступ запрещен")
        else:
            return object.__getattribute__(self, __name)

    # Вызывается автоматически, при изменении свойства key (self, key, value)
    def __setattr__(self, __name, __value):
        if __name == 'z': # Такой атрибут нельзя создать
            raise ValueError("Недопустимое значение")
        else:
            print(f"Зачем это мне: {__value}")
            # если self.x = value это будет рекурсия
            object.__setattr__(self, __name, __value)

    def __getattr__(self, item):
        print("Что за... Такого атрибута ведь нет")
        return False # Ошибка по умолчанию

    # При удалении атрибута
    def __delattr__(self, __name):
        print('__delattr__: ' + __name)
        object.__delattr__(self, __name)


    # Не правильно т.к сздают новый атрибут для экземпляра а не меняет атрибут класса
    def set_bound(self, left):
        self.MIN_COORD = left  

    # Nice:
    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left  


pt1 = Point(1, 2)
pt2 = Point(10, 20)
print(pt1.y)
print(pt1.yy)
print(pt1.__dict__)
# print(Point.__dict__)
# a = pt1.x
del pt1.x
print(pt1.__dict__)
