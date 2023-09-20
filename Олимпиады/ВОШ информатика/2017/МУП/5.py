N, xEn, yEn = map(int, input().split(' '))

minS = 1000000
for i in range(N):
    coord = list(map(int, input().split(' ')))
   


    if True:
        a = ((coord[0]-coord[2])**2+(coord[1]-coord[3])**2)**0.5
        b = ((coord[0]-coord[4])**2+(coord[1]-coord[5])**2)**0.5
        c = ((coord[2]-coord[4])**2+(coord[3]-coord[5])**2)**0.5
        p = (a+b+c)/2
        S = (p*(p-a)*(p-b)*(p-c))**5
        minS = min(S, minS)

