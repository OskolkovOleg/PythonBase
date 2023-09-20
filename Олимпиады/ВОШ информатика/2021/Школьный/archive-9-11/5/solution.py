a = int(input())
b = int(input())
if a == 1:
    print(1)
elif a == b:
    print(-1)
else:
    print((b - 2) // (b - a) * a)
