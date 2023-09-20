N = int(input())
matrRoads = [list(map(int, input().split(' '))) for i in range(N)]
print(matrRoads)
odn = 0
dv = 0
for i in range(N):
    for j in range(i+1,N):
        if i != j:
            if matrRoads[i][j] == matrRoads[j][i] == 1:
                dv += 1
            elif matrRoads[i][j] == 1 or matrRoads[j][i] == 1:
                odn += 1

print(odn)
print(dv)