# N1 = int(input())
# arrK1 = [list(map(int, input().split())) for i in range(N1)]

# N2 = int(input())
# otv = [0, [0, 0], [0, 0]]
# for i in range(N2):
#     coord = list(map(int, input().split(" ")))
#     for (x, y) in arrK1:
#         lenV = ((coord[0]-x)**2 + (coord[1]-y)**2)**0.5
#         if lenV > otv[0]:
#             otv[0] = lenV
#             otv[1] = [x, y]
#             otv[2] = [coord[0], coord[1]]

# print(' '.join(list(map(str, otv[1]))),"\n", ' '.join(list(map(str,otv[2]))))

N1 = int(input())
arrK1 = [list(map(int, input().split())) for i in range(N1)]

N2 = int(input())
arrK2 = [list(map(int, input().split())) for i in range(N1)]
otv = [0, [0, 0], [0, 0]]
for coord in N2:
    for (x, y) in arrK1:
        lenV = ((coord[0]-x)**2 + (coord[1]-y)**2)**0.5
        if lenV > otv[0]:
            otv[0] = lenV
            otv[1] = [x, y]
            otv[2] = [coord[0], coord[1]]

print(' '.join(list(map(str, otv[1]))),"\n", ' '.join(list(map(str,otv[2]))))
