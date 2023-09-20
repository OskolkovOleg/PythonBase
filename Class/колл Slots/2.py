# __slots__

# class Point2D:
#     __slots__ = ("x", "y", "__length")

#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y
#         self.__length = (x ** 2 + y ** 2) ** 0.5

#     @property
#     def lenght(self):
#         return self.__length

#     @lenght.setter
#     def lenght(self, value):
#         self.__length = value

# p = Point2D(1, 2)
# p.lenght = 3


class Point2D:
    __slots__ = ("x", "y")

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y



class Point3D(Point2D):
    # pass
    # __slots__ = () # Только сво-ва класса родителя
    __slots__ = 'z', 

pt3 = Point3D(1, 2)
pt3.z = 30
# print(pt3.__dict__)
print(pt3.__slots__)