d,sumTime = map(int,input().split())
minTimes = [0]*d
maxTimes = [0]*d
for i in range(d):
    minTimes[i],maxTimes[i] = map(int,input().split())

if sum(maxTimes) < sumTime or sum(minTimes) > sumTime:
    print('NO')
else:
    print('YES')
    
    ans = []
    for i in range(d):
        ans.append(minTimes[i])
        sumTime-=minTimes[i]

    for i in range(d):
        
        if sumTime - maxTimes[i]-minTimes[i]<0:
            ans[i] += sumTime
            print(ans[i],end = ' ')
            break
        sumTime -= maxTimes[i]-minTimes[i]
        ans[i] += maxTimes[i]-minTimes[i]

        print(ans[i],end = ' ')
    

    
     