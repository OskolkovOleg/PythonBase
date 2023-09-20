def gcdex(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcdex(b, a % b)
        return d, y, x - a // b * y

def inv(a, m):
    d, x, y = gcdex(a, m)
    return x


a = int(input())
b = int(input())

print((1 * b * inv(b, a) - 1 * a * inv(a, b)) % (a * b))

