v1 = [1, 2, 3]
v2 = [2, 3]
# v2 = [2, 3, 2332]


class DefenderVector():
    def __init__(self, v) -> None:
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]  # Создаем копию
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp

        return False  # Если False исключения обрабатываться будут


try:
    with DefenderVector(v1) as dv:
        for i, a in enumerate(dv):
            dv[i] += v2[i]
except:
    pass
print(v1)
