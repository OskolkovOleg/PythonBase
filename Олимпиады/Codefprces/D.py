n, wo, ho = map(int,input().split())
conv = []
for i in range(n):
    conv.append(list(map(int,input().split()))) 

maxConv = max(conv)
conv.remove(max(conv))
ans = 0
if maxConv[0]>wo and maxConv[1]>ho:
    ans += 1
    for i in conv:
        t = max(conv)
        if t[0] > wo and t[1]<ho:
            if t<maxConv:
                maxConv = t
                ans+=1
                conv.remove(t)
            else:
                conv.remove(t)
        else:
            break
    
    print(ans)
else:
    print(0)
