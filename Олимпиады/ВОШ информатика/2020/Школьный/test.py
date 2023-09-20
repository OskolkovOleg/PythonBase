# n = int(input())
# ans = []
# for i in range(n):
#   a = int(input())
#   if not a in ans:
#     ans.append(a)
#   elif a in ans:
#     ans.remove(a)
# if len(ans) != 0
#   print(min(ans))
# else:
#   print(-1)
# n = int(input())
# k = 0
# while n!=0:
#     flag = True
#     for i in str(n):
#         print(i)
#         if int(i)%2!=0:
            
#             flag = False
        
            
#     if flag:
#         n//=2
#     else:
#         n-=1
#     k+=1
# print(k)
# a = int(input())
# b = int(input())
# n = int(input())
# x = []
# ans = 0
# sh = 0
# for i in range(n):
#   p = int(input())
#   if p<=a:
#     sh += 1
#   if p>b:
#     ans+=1
#     continue
  
#   x.append(p)

# if sh> len(x)-sh:
#     print(int(-1 * len(x) // 2 * -1)+ans)
# else:
#   print(max(sh, len(x)-sh)+ans)

P = int(input())
if P<=6:
  print(0)
else:
  n = P//2
  k = n-1
  print(k)
