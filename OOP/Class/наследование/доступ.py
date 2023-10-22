class Geom:
    name = "Geom"

    def __init__(self, x1, x2, y1, y2) -> None:
        self._x1 = x1
        self._x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        print("Инициализатор", self.__class__)


class Rect(Geom):
    def __init__(self, x1, x2, y1, y2, fill) -> None:
        super().__init__(x1, x2, y1, y2) 
        self.fill = fill
        print("Инициализатор Rect")

    def get_coord(self):
        # 
        return (self._x1, self._x2) 
        return (self.__y1, self.__y2)

r = Rect(1, 2, 3, 4, '')
print(r.get_coord())
print(r.__dict__)