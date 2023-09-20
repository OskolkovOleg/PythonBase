h = int(input())
a = int(input())
b = int(input())
ans = h - a + b
if ans < 0:
    ans += 24
print(ans)

