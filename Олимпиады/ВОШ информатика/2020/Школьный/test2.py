# while True:
#     n = int(input())
#     ans = n//(3+2)
#     if n % 5 != 0:
#         ans +=1
#     if n<=3:
#         ans = -1
#     print(ans)

# n = int(input())
# m = int(input())
# if n in [0,1,2] or m in [0,1,2]:
#     print(0)

# elif m>n:
#     if n%2==0:
#         print((m-n+2)*2)
#     else:
#         print((m-n+1))

# else:
#     if m%2==0:
#         print((n-m+2)*2)
#     else:
#         print((n-m+1)*1)

# n = int(input())
# m = int(input())

# ost = n+1
# osts = []
# while ost != 0:
#     if m > ost:
#         ost-=1
#     else:
#         ost = m
#         osts.append(ost)
#         break
#     m -= ost
#     osts.append(ost)
# if osts[-1] == 0:
#     print(0)
# else:
#     for i in osts:
#         print(i)

n1 = int(input())
m = int(input())
a1 = n1+m-2
n = (m+n1+1)//4
an = a1-4 *(n-1)
sn = (((a1+an)*n)//2)
print(sn+n1)


# n = int(input())
# arr = [list(input()) for i in range(n)]
# for i in arr:
#     if not "#" in i:
#         arr.remove(i)

# def bar(index, arr):
#     return [i[index] for i in arr]


# c = bar(0, arr)
# if not "#" in c:
#     for i in range(len(arr)):
#         arr[i] = arr[i][1:]

# c = bar(-1, arr)
# if not "#" in c:
#     for i in range(len(arr)):
#         arr[i] = arr[i][:-1]

# flag1 = True
# flag2 = False
# flag3 = False
# flag4 = False
# flag5 = False
# flag6 = False

# for i in range(len(arr)-1):
#     if not (arr[i] == arr[i+1] and flag1 and (not '.' in arr[i])):
#         flag1 = False

# if arr[1] == arr[-1] and not '.' in bar(0, arr):
#     if '.' in arr[1] \
#             and (not '.' in bar(0, arr)) \
#             and (not '.' in bar(-1, arr)):
#         for i in arr:
#             if not '.' in i:
#                 flag5 = True
#     elif bar(0, arr) == bar(-1, arr) :
#         flag2 = True
#         for i in range(1,len(arr)-2):
#             if arr[i] == arr[i+1] or not flag2:
#                 flag2 = True
#             else:
#                 flag2 = False
#     else:
#         flag3 = True
#         for i in range(1,len(arr)-2):
#             if arr[i] == arr[i+1] or not flag3:
#                 flag3 = True
#             else:
#                 flag3 = False

# else:
#     if not '.' in bar(0, arr) and not '.' in arr[-1]:
#         flag4 = True
#         for i in range(len(arr)-2):
#             if arr[i] == arr[i+1] or not flag4:
#                 flag4 = True
#             else:
#                 flag4 = False 
#     elif not '.' in bar(0, arr) \
#             and not '.#' in bar(-1, arr) \
#             and not '.' in arr[0] \
#             and arr[0] in arr[1:]:
        
#         flag6 = True

    

# if flag1:
#     print('I')
# elif flag2:
#     print('O')
# elif flag3:
#     print('C')
# elif flag4:
#     print('L')
# elif flag5:
#     print('H')
# elif flag6:
#     print('P')
# else:
#     print('X')



            
    

    


