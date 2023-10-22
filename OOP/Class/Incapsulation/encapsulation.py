class Point:
    def __init__(self, x,y):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(x):
            self.__x = x
            self.__y = y
        # self.__x = x # Только внутри класса
        # self.__y = y # Только внутри класса
        # self._y = y # Сигнал, что лучше не вызывать из вне
        # self.c = 5  # Свободное использование

    @classmethod
    def __check_value(cls,x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(x):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами!')
    
    def get_coord(self):
        return self.__x, self.__y


pt = Point(1,2)
# print(pt.__x,pt._y,pt.c)
(pt.set_coord(3,2))
