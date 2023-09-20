n, k = map(int, input().split())
a = list(map(int, input().split()))

two = a.count(2)
one = n + k - two
if one > two:
    print(two + one - two)
elif two > one:
    print(one + (two - one)//2 + (two - one)%2)
else:
    print((one+two)//2)

