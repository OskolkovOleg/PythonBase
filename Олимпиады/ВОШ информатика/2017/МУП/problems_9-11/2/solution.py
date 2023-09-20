m = int(input())
n4 = m % 3
n3 = (m - 4 * n4) // 3
if n3 >= 0:
    print(n3)
    print(n4)
else:
    print(0)
    print(0)
