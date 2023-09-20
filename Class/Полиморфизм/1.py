class Geom:
    # Имитация абстрактного метода
    def get_pr(self):
        raise NotImplementedError("В дочернем классе должен быть определен метод get_pr")
        # return -1

class Rect(Geom):
    def __init__(self, w, h) -> None:
        self.w = w
        self.h = h

    def get_pr(self):
        return 2*(self.w+self.h)


class Square(Geom):
    def __init__(self, a: int) -> None:
        self.a = a

    def get_pr(self):
        return 4*self.a


class Triangle(Geom):
    def __init__(self, a, b, c, ) -> None:
        self.a = a
        self.b = b
        self.c = c

    # def get_tr_pr(self):
    #     return self.a + self.b + self.c

    # def get_pr(self):
    #     return self.a + self.b + self.c

r1 = Rect(1, 2)
r2 = Rect(3, 4)
s1 = Square(10)
s2 = Square(20)
t1 = Triangle(1, 2, 3)
t2 = Triangle(4, 5, 6)

geom = [r1, r2, s1, s2, t1, t2]
for g in geom:
    print(g.get_pr())

# print(r1.get_rect_pr(), r2.get_rect_pr())
# print(s1.get_sq_pr(), s1.get_sq_pr())
