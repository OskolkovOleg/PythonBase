# __eq__() __ne__() __lt_() __le__() __gt__() _ge__()

class Clock:
    __DAY = 86400

    def __init__(self, seconds: int) -> None:
        if not isinstance(seconds, int):
            raise TypeError(
                "Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, int | Clock):
            raise ArithmeticError(
                "Правый операнд долженбыть int или Clock")
        
        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        return self.seconds == self.__verify_data(other)

    def __lt__(self, other):
        return self.seconds < self.__verify_data(other)

    def __le__(self, other):
        return self.seconds <= self.__verify_data(other)

c1 = Clock(1000)
c2 = Clock(1200)
print(c1 == c2) # По умолчанию сравнив id
print(c1 != c2) # Интерпретатор дел так: not(c1 == c2)
print(c1 < c2) # По умолчанию ошибка
print(c1 > c2) # По умолчанию переделывает на c1 < c2 если нет __gt__()
print(c1 <= c2)
print(c1 >= c2)
