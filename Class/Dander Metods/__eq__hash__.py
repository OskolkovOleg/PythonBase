# __eq__() __hash__()

# print(hash(123))
# print(hash('Python'))
# print(hash('Python'))
# Для одинаковых объектов hash одинаковый, но одинаковый hash не значит что объекты  одинаковые
# Только для constant


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

p1 = Point(1, 2)
p2 = Point(1, 2)

# Когда переопределяем eq hash все заканч, но переопр hash
print(hash(p1), hash(p2), sep="\n") 
print(p1 == p2)

# Что дает:
# Воспринимаются как один ключ
d = {}
d[p1] = 1
d[p2] = 2
print(d)