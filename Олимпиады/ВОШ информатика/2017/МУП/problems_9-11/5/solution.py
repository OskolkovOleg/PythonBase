n = int(input())
k = int(input())
d = dict()
d[n] = 1
while k > 0:
    m = max(d.keys())
    count = min(k, d[m])
    del d[m]
    k -= count
    ans1 = (m - 1) // 2
    ans2 = m - 1 - ans1
    d[ans1] = d.get(ans1, 0) + count
    d[ans2] = d.get(ans2, 0) + count
print(ans1)
print(ans2)
