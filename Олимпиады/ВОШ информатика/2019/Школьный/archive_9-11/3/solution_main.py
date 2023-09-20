a = int(input())
b = int(input())

if a >= b:
    ans = 1
    while ans % b != b - 1:
        ans += a
else:
    ans = b - 1
    while ans % a != 1:
        ans += b
assert 1 <= ans <= 2e9
print(ans)
