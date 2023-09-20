import time
start_time = time.time()


for i in range(10,34):
    with open(f'archive_9-11/4/tests/{i}', 'r') as f:
        #s =int(f.readline().strip())
        #K =int(f.readline().strip())
        n =int(f.readline().strip())
        #p = [int(f.readline().strip()) for i in range(N)]
    with open(f'archive_9-11/4/tests/{i}.a', 'r') as f2:
        otv = f2.readline().strip().split(' ')
    start_time = time.time()
   


    motv = []

    print(i, end='')
    print("--- %s seconds ---" % (time.time() - start_time),end='')
    print(True if motv == otv else False,motv, otv)