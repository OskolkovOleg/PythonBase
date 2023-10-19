# __iter__() __next__()

# ist = [8, 5, 6, 1, 7]
# it = iter(ist)
# print(next(it))

class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0) -> None:
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


fr = FRange(0, 2, 0.5)
# print(next(fr))
# print(next(fr))
# print(next(fr))
# print(next(fr))

it = iter(fr)
for i in fr:
    print(i)


class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5) -> None:
        self.rows = rows
        self.fr = FRange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration


fr = FRange2D(0, 2, 0.5, 5)
for i in fr:
    for i in i:
        print(i, end=' ')
    print()
