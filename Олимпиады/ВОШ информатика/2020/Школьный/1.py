import time
start_time = time.time()



for i in range(10,12):
    with open(f'archive_9-11/1/tests/0{i}', 'r') as f:
        #s =int(f.readline().strip())
        K =int(f.readline().strip())
        N =int(f.readline().strip())
        #p = [int(f.readline().strip()) for i in range(N)]
    with open(f'archive_9-11/1/tests/0{i}.a', 'r') as f2:
        otv = int(f2.readline())
    start_time = time.time()
   
    a1 = abs((N//K)*K-N)
    a2 = abs((N//K+1)*K-N)
    motv = min(a1,a2)

    print(motv, end='')
    print("--- %s seconds ---" % (time.time() - start_time),end='')
    print(True if motv == otv else False)
    