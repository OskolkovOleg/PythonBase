import math
from abc import ABC
from abc import abstractmethod

# Абстрактный класс - это некий шаблон, 
# он не может иметь объекты, 
# он должен содержать абстрактные методы, 
# которые нужно обязательно реализовывать в наследниках
# Для создания абстрактов можно использовать raise при вызове методов
# Но лучше использовать ABC
class Shape(ABC):

    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        print("calc perimetr")
    
    def drag(self):
        print("Basic draging functionality")


class Triangle(Shape):

    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def draw(self):
        print(f"Drawing triangle with sides={self.a}, {self.b}, {self.c}")\

    def area(self):
        s = (self.a + self.b + self.c)
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def drag(self):
        print('Additional actions')
        return super().drag()

t = Triangle(10, 10, 10)