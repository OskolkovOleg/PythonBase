import timeit
import numpy

value = 100_000_000


def loop1() -> int:
    num = 0
    result = 0
    while num < value:
        result += 1
        num += 1
    return result


def loop2() -> int:
    result = 0
    for num in range(value):
        result += num
    return result


def loop3() -> int:
    return sum(range(value))


def loop4() -> int:
    return numpy.sum(numpy.arange(value))

print(f"loop1: {timeit.timeit(loop1, number=1)}")
print(f"loop2: {timeit.timeit(loop2, number=1)}")
print(f"loop3: {timeit.timeit(loop3, number=1)}")
print(f"loop4: {timeit.timeit(loop4, number=1)}")



