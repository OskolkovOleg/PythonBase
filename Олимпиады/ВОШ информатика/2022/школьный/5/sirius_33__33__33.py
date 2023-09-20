import time
start_time = time.time()



for i in range(1,16):
    with open(f'5/tests/{i}', 'r') as f:
        #s =int(f.readline().strip())
        
        N = int(f.readline().strip())
        a = [list(f.readline().strip()) for i in range(N)]
    with open(f'5/tests/{i}.a', 'r') as f2:
        otv = f2.readline().strip()
    start_time = time.time()
    #########################################

    #########################################
    
    # N = int(input())
    # a = []
    x1 = ''
    x2 = ''
    x3 = ''
    x4 = ''
    # for i in range(0,N):
    #     x = input()
    #     a.append(x)

    k = a[0]
    for i in range(0,N):
        X = k[i]
        x1 += X
    k = a[-1]
    for i in range(0,N):
        X = k[i]
        x2 += X
    for i in range(0,N):
        k = a[i]
        X = k[0]
        x3 += X
    for i in range(0,N):
        k = a[i]
        X = k[-1]
        x4 += X
    g = (N//2) + 1
    G = a[g]
    count=0
    for i in range(0,N):
        q = G[i]
        if q == '#':
            count+=1
    X1 = a[1]
    
    if x1 == x2 and x3 == x4 and X1 != x1:
        motv='O'
    elif x1 == x2 and x3 != x4:
        motv='C'
    elif x3 == x4 and x1 == x2 and G == count :
        motv='H'
    elif x1 == x3 and x2 != x4:
        motv='P'
    elif x1 != x2 and x3 != x4:
        motv='L'
    elif x1 == X1:
        motv='I'
    else:
        motv='X'
    
    #########################################
    
    #########################################

    print(motv, end='')
    print("--- %s seconds ---" % (time.time() - start_time),end='')
    fl = False
    print(True if motv == otv else (False,otv))
    if motv != otv:
        for i in a:
            for j in i:
                print(j, end = ' ')
            print()


    
                

