# self может ссылаться на объекты дочерних классов

class Geom:
    name = "Geom"

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        # self.draw() Но так делать точно не надо

    def draw(self):
        print("Рисование примитивы")

class Line(Geom):
    def draw(self):
        print("Рисование линии")

    # def set_coords(self, x1, y1, x2, y2):
    #     self.x1 = x1
    #     self.x2 = x2
    #     self.y1 = y1
    #     self.y2 = y2


class Rect(Geom):
    name = "line"

    # def draw(self):
    #     print("Рисование линии")

    # def set_coords(self, x1, y1, x2, y2):
    #     self.x1 = x1
    #     self.x2 = x2
    #     self.y1 = y1
    #     self.y2 = y2


l = Line()
r = Rect()
print(l.set_coords(1, 1, 1, 1))
print(r.set_coords(1, 1, 1, 1))
print(r.__dict__)
print(r.name)
print(l.name)
l.draw()
r.draw()

