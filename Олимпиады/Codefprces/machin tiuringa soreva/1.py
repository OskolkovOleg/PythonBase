
n = int(input())
k = int(input())
t = int(input())

ada = k - t
ost = n % ada

print(ost + t if ost != 0 else k)