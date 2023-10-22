# __add__() __mul__() __truediv__() __sub__() __floodiv__() __mod__()

class Clock:
    __DAY = 86400

    def __init__(self, seconds: int) -> None:
        if not isinstance(seconds, int):
            raise TypeError(
                "Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self) -> str:
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    # other ссылается на значение справа от +
    def __add__(self, other):
        if not isinstance(other, int | Clock):
            raise ArithmeticError(
                "Правый операнд долженбыть int или Clock")
        if isinstance(other, Clock):
            return Clock(self.seconds + other.seconds)
        return Clock(self.seconds + other)
    
    def __radd__(self, other):
        return self + other
    
    def __iadd__(self, other):
        if not isinstance(other, int | Clock):
            raise ArithmeticError(
                "Правый операнд долженбыть int или Clock")
        self.seconds += other
        return self


inp1 = "22:10".split(":")
inp2 = "53"

c1 = Clock(int(inp1[0])*3600+int(inp1[1])*60+int(inp2)*60)
print(c1.get_time())




# c1 = Clock(1000)
# c2 = Clock(2000)
# c1.seconds = c1.seconds + 100
# print(c1.get_time())
# # Типо подругому при помощи выш описанных методов
# c1 = c1 + 100
# print(c1.get_time())
# c3 = c1 + c2

# print(c3.get_time())


# c1 = 100 + c1 # Пытаемся у int вызвать add и сложить для этого radd
# print(c1.get_time())

# c1 += 100 # Пытаемся у int вызвать add и сложить для этого iadd
# print(c1.get_time())