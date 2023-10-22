x, y = (1, 2)
print(x, y)

x, *y = (1, 2, 3, 4, 4)
print(x, y)

x, *y, z = (1, 2, 3, 4, 4)
print(x, y, z)


x, *y, z = [None, "he", 1, 2.3, [23]]
print(x, y, z)


x, *y, z = "Hello Python"
print(x, y, z)

*y, z = 1, 2, 3, 4
print(y, z)

a = [1, 2, 3]
print((a, ))
print((*a, ))

d = -5, 5
print(d)
print(list(range(*d)))
print([range(*d)])
print([*range(*d)])
print(*range(*d))

print(*range(*d), *(True, False), *a)


d = {0: "Безнадежно", 1: "ужасно", 2: "неуд.", 3: "удовл.", 4: "Хорошо", 5: "Отлично"}
print({*d})
print({*d.values()})
print({*d.items()})


d2 = {6: "превосходно", 7: "элитарно", 8: "божественно",}
print({**d, **d2})

