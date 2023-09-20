N = int(input())
name = input()
ans = 0
for i in range(N):
  for j in name[i:]:
    if name[i]!=j and ord(name[i])<ord(j):
      ans+=1
print(ans)