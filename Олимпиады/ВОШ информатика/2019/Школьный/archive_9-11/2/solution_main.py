import sys
a = int(input())
b = int(input())

if a % 2 == 0:
    a1 = a + 1
    a2 = a
    a1 = a + 1
else:
    a1 = a
    a2 = a + 1

if b % 2 == 0:
    b1 = b - 1
    b2 = b
else:
    b1 = b
    b2 = b - 1

s = 0
if a2 <= b2:
    s += (b2 + a2) // 2 * ((b2 - a2) // 2 + 1)
if a1 <= b1:
    s -= (b1 + a1) // 2 * ((b1 - a1) // 2 + 1)

print(s)
