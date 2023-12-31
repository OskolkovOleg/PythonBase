# Нарушение принципа в подклассе Square

class Recrangle:
    def __init__(self, width, height) -> None:
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Width: {self.width}, height: {self.height}"

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


class Square(Recrangle):
    def __init__(self, size) -> None:
        super().__init__(size, size)

    @Recrangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Recrangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc):
    w = rc.width
    rc.height = 10 #Побочный эффект, меняется и ширина
    expected = int(w*10)
    print(f"Expected an area of {expected}, got {rc.area}")


rc = Recrangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)