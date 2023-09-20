import time

for j in range(10,12):
    with open(f'archive_9-11/5/tests/{j}', 'r') as f:
        #s =int(f.readline().strip())
        #K =int(f.readline().strip())
        n = int(f.readline().strip())

        a = [int(f.readline().strip()) for i in range(n)]
    with open(f'archive_9-11/5/tests/{j}.a', 'r') as f2:
        otv = [int(f2.readline().strip()) for i in range(n)]

    start_time = time.time()
    # motv = [1]
    # flag = False
    # for i in range(len(a)-2,-1,-1):
    #     #print(ai[i],sum(ai[:i+1]),ai[i+1])
    #     if sum(a[:i+1])>a[i+1] and not flag:
    #         motv.append(1)
    #     else:
    #         motv.append(0)
    #         flag = True

        
    # motv = motv[::-1]
   
    ans = [0] * n
    motv = []
    s = 0
    for i in range(n - 1):
        if a[i] > a[0] and a[i] + s > a[i + 1]:
            ans[i] = 1
        else:
            ans[i] = 0
        s += a[i]
    if a[n - 1] > a[0]:
        ans[n - 1] = 1

    else:
        ans[n - 1] = 0
    i = n - 1
    while ans[i] == 1:
        i -= 1
    while i >= 0:
        ans[i] = 0
        i -= 1
    if n == 1:
        ans = [1]
    for i in range(n):
        motv.append(ans[i])


    

    print(j, end='')
    print("--- %s seconds ---" % (time.time() - start_time),end='')
    print(True if motv == otv else (False,motv, otv))