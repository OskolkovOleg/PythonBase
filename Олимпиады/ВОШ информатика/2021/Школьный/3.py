import time
start_time = time.time()



for i in range(10,27):
    with open(f'archive-9-11/3/tests/{i}', 'r') as f:
        s =int(f.readline().strip())
        e =int(f.readline().strip())
        N =int(f.readline().strip())
    with open(f'archive-9-11/3/tests/{i}', 'r') as f:
        p = [int(f.readline().strip()) for i in range(N+3)]
        s =p[0] #int(input())
        e =p[1] #int(input())
        N =p[2] #int(input())
        p = p[2:-1]
    with open(f'archive-9-11/3/tests/{i}.a', 'r') as f2:
        otv = int(f2.readline().strip())
    start_time = time.time()





    xp = [p[i] for i in range(N)]
    a1 = min([abs(xp[j]-s) for j in range(N)])
    a1 = min([abs(xp[i]-s) for i in range(N)])
    a3 = min([abs(xp[i]-e) for i in range(N)])
    motv = min(a1+a3+1,abs(e-s))





    print(motv, end='')
    print("--- %s seconds ---" % (time.time() - start_time),end='')
    print(True if motv == otv else False)
    
