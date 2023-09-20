# A, B = (map(int, input().split(' ')))
# # # if A%2!=0 or B%2!=0:
# # #     print(round((A*B-(A**2+B**2)**0.5)//2))
# # # else:
# # print(round((A*B-(A**2+B**2)**0.5//1)//2)+1)
#     # print((A*B)//2-max(A,B)//2)


# y = a*x + b

# 0 = a*B + A
# -A = a*B
# a = -A/B
# b = A
# a = -A/B

# y = (-A/B)*x + A

A, B = (map(int, input().split(' ')))
summa = 0
for x in range(1,B):
    y = (-A/B)*x + A
    summa += y//1
    print(y)
print(int(summa))


