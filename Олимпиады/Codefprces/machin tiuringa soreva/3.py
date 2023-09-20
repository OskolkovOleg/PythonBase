n = int(input())
a = list(map(int, input().split()))
import math

border = min(a)

for i in a:
    if i%border!=0:
        border = math.gcd(i, border)
        
else:
    print(border-1)

