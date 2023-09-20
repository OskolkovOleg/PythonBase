import time
start_time = time.time()



for i in range(10,27):
    with open(f'archive_9-11/3/tests/{i}', 'r') as f:
        #s =int(f.readline().strip())
        #K =int(f.readline().strip())
        N =int(f.readline().strip())
        
        a = [None]*N
        
        
        #int(f.readline().strip()) for i in range(N)
        for k in range(N):
            
            
            a[int(f.readline().strip())-1]=k

    with open(f'archive_9-11/3/tests/{i}.a', 'r') as f2:
        
        #print(a)
        otv = [int(f2.readline().strip()) for h in range(N)]
    start_time = time.time()
    
    
    mot = a[::-1]
    motv = [mot.index(i)+1 for i in range(N)]

    #print(i,a,mot,motv, end='')
    print("--- %s seconds ---" % (time.time() - start_time),end='')
    print(True if motv == otv else False, otv)
    