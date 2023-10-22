class Point3D:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError(
                "Координата должна быть целым числом")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, coord):
        self.verify_coord(coord)
        self.__x = coord

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, coord):
        self.verify_coord(coord)
        self.__y = coord

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, coord):
        self.verify_coord(coord)
        self.__z = coord


p = Point3D(1, 2, 3)
print(p.__dict__)

# функциональное дублирование