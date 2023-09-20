# __getitem__()  __setitem__()  __delitem__()
class Student:
    def __init__(self, name, marks) -> None:
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if not 0 <= item < len(self.marks):
            raise IndexError("Неверный индекс")
        return self.marks[item]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть типа int")
        if key >= len(self.marks):
            off = key+1 - len(self.marks)
            self.marks.extend([None]*off)
        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть типа int")
        
        del self.marks[key]

s1 = Student("Сергей", [5, 5, 3, 2, 5])
print(s1[2])
s1[22] = 3213
del s1[2]
print(s1.marks)
