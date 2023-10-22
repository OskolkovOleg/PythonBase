from typing import Union


#3.8
def square(number: Union[int, float]) -> Union[int, float]:
    return number ** 2


#3.10
def square(number: int | float) -> float | int:
    return number ** 2


a = 1
print(isinstance(a, int))
print(isinstance(a, int | str))
print(isinstance(a, float | str))

a = 145
print(bin(a))
print(a.bit_count())


with (
    open("1.txt", "r") as read_file,
    open("1.txt", "w") as write_file,
    ): pass


