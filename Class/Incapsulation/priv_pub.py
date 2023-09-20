# Я дурак написал и случайно удалил
from accessify import private, protected

class Point:

    @private # еще круче чем __
    @classmethod
    def check_value(cls, x):
        return type(x) in (int, float)

    def __noncheck_value(cls, x):
        return type(x) in (int, float)

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0

        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x  
            self.__y = y
        else:
            raise ValueError(
                "Координаты должны быть числами")

    def get_сoord(self):
        return self.__x, self.__y

pt = Point(1, 2)
# print(pt._Point__noncheck_value(5)) # Наверное раньше работало