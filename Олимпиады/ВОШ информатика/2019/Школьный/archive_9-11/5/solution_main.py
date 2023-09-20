import sys
n = int(input())
m = int(input())
k = int(input())

if k == n * m -1:
    print("IMPOSSIBLE")
    sys.exit(0)
if k == n * m:
    print(("R" * m + "\n") * n)
    sys.exit(0)
if m == 1:
    print("D")
    for i in range(n * m - k - 1):
        print("U")
    for i in range(k):
        print("R")
    sys.exit(0)

for i in range(n):
    for j in range(m):
        if i * m + j < n * m - k:
            if i == 0:
                if j == 0:
                    print('R', end='')
                else:
                    print('L', end='')
            else:
                print('U', end='')
        else:
            print('R', end = '')
    print()

