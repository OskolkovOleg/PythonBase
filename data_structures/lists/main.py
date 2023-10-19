# # рассмотрим списки они же массивы
# # переменные можно называть по русски

# s = [] # Создание пустого списка
# s2 = [1, 2, 3, 4, 's2', [1,2], 5, 6]

# # Можно преобразовывать объекты в списки
# s3 = list('список') #s3 = ['с', 'п', 'и', 'с', 'о', 'к']

# s4 = list(range(10))        # Обнаружил случайно
# s5 = [c for c in range(10)] # Но помоему цикл быстрее функции

# print(s4)
# print(s5)


# values = [False, False, True]
# values2 = [True, True, True]
# values3 = [False, False, False]

# print(all(values))
# print(all(values2))
# print(all(values3))

# print(any(values))
# print(any(values2))
# print(any(values3))


# values = [None, 1, 2]
# values2 = [-2, 1, 4]
# values3 = [0, 4, 1]

# print(all(values))
# print(all(values2))
# print(all(values3))


# values = [[1, 2], [3], [4, 5], [6, 7, 8, 9]]
# print(sum(values, []))


# import itertools

# values = [[1, 2], [3], [4, 5], [6, 7, 8, 9]]
# print(list(itertools.chain.from_iterable(values)))


# values = [1, 2, 3]

# print(', '.join(map(str, values)))


# data = [
#     (1, 2),
#     (3, 4),
#     (5, 6)
# ]

# print(*data)
# result = zip(*data)
# print(list(result))


# values = [1,5,2,3,4,3]
# print(list(set(values))) # Не сохраняет порядок а сортрует

# from collections import OrderedDict
# print(list(OrderedDict.fromkeys(values).keys()))


server1 = "server_2"
server2 = None
server3 = None
server4 = "server_4"


result = server1 or server2 or server3 or "servers_are_busy"
result2 = server1 and server2 and server3 and "servers_are_busy"

print(result)
print(result2)