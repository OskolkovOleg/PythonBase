class Geom:
    name = "Geom"

    def __init__(self, x1, x2, y1, y2) -> None:
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        print("Инициализатор", self.__class__)



class Line(Geom):
    
    def draw(self):
        print("Рисование линии")


class Rect(Geom):
    def __init__(self, x1, x2, y1, y2, fill) -> None:
        # Возвращает ссылку на объект посредник
        # Вызывать в самую первую очередь есть баги!!!!!!
        # Называется делегированием
        super().__init__(x1, x2, y1, y2) 
        self.fill = fill
        print("Инициализатор Rect")

    def draw(self):
        print("Рисование Rect")


l = Line(1, 2, 3, 4)
r = Rect(1, 2, 3, 4, '')
print(r.__dict__)
