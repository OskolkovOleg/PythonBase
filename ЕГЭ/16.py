# def f(n: int) -> int:
#     if n > 30:
#         return n * n + 3 * n + 5
#     elif n % 2 == 0:
#         return 2 * f(n+1) + f(n+4)
#     return f(n+2) + 3*f(n+5)

# s = 0
# for n in range(1, 1001):
#     if str(f(n)).count("0") >= 2:
#         s += 1

# print(s)

# def F(n: int) -> int:
#     if n <= 15:
#         return 2 * n * n + 4 * n + 3
#     elif n % 3 == 0:
#         return F(n-1) + n * n + 3
#     return F(n-2) + n - 6

# s = 0
# for n in range(1, 1001):
#     if all([int(x)%2 != 0 for x in str(F(n))]):
#         s += 1

# print(s)


def F(n: int):
    if n < 3:
        return n + 1
    if n % 2 == 0:
        return n + 2*F(n + 2)
    return F(n - 2) + n - 2


s = 0
for n in range(0, 1_000_000):
    try:
        a = F(n)
    except:
        continue
    if a >= 1000:
        break
    if len(str(a)) == 3:
        print(n, a)
        s += 1

print(s)

# def F(n: int):
#     if n <= 1:
#         return n
#     if n % 3 == 0:
#         return n + F(n / 3)
#     return n + F(n + 3) 


# s = 0
# for n in range(0, 1_000_000):
#     try:
#         a = F(n)
#     except:
#         continue
#     if a >= 100:
#         print(n, a)
#         break

# print(s)