from enum import Enum
from math import *


# # ##############################
# # Это Антипаттерн Лютое нарушение принципа Открытости Закрытости
# # Неудобно и ужасно
# class CoordinatesSystem(Enum):
#     CARTESIAN = 1
#     POLAR = 2


# class Point:
#     def __init__(self, a, b, system=CoordinatesSystem) -> None:
#         if system == CoordinatesSystem.CARTESIAN:
#             self.x = a
#             self.y = b
#         elif system == CoordinatesSystem.POLAR:
#             self.x = a * cos(b)
#             self.y = a * sin(b)
# # ##############################

# Паттерн фабричный метод
# Это любой метод который создает объект 
# альтернатива конструктору, с множеством преимуществ
# Мы получаем хороший nameing
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
   
    def __str__(self) -> str:
        return f"{self.x=} {self.y=} "

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)
    
    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))

if __name__ == "__main__":
    p = Point(2, 3)
    p2 = Point.new_polar_point(1, 2)
    print(p, p2)