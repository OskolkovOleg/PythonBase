def section(k):
    if k <= 36:
        return (k - 1) // 4
    else:
        return 8 - (k - 37) // 2

count = [0] * 9
n = int(input())
for i in range(n):
    count[section(int(input()))] += 1
ans = 0
curr = 0
for i in range(9):
    if count[i] == 6:
        curr += 1
        ans = max(ans, curr)
    else:
        curr = 0
print(ans)

