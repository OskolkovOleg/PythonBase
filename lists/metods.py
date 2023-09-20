a = [1, 2, 3, 435, 234, 2, 3, 21, 23, 4536, 5, 46]
a.insert(3, -1000)
print(a)

a.remove(-1000)# Удаляет елемент по значению
print(a)

print(a.pop(3))# Удаляет елемент по индексу

print(a.copy())
print(a[:])

print(a.count(3))

print(a.index(3))
print(a.index(3, 3)) 

print(sorted(a))

a.reverse()
print(a)

a.sort()
print(a)

a.sort(reverse=True)
print(a)

a.extend([1,2,23])
print(a)

a.extend([None]*100)
print(a)