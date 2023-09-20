from wsgiref.validate import InputWrapper


n = int(input())
names = ['']*n
ans = []
for i in range(n):
    inp = input()
    if names.count(inp) == 0:
        ans.append("OK")
        names.append(inp)
    else:
        
        for k in range(1,n+1):
            if names.count(inp+str(k))==0:
                names.append(inp+str(k))
                ans.append(inp+str(k))
                break
for i in ans:
    print(i)
    
    
