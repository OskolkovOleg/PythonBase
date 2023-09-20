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
   
    if round(n**0.5)**2%2==0:
        if round(n**0.5)**2<n:
            Nl = round(n**0.5)+1
            Nb = n-round(n**0.5)**2
        elif round(n**0.5)**2>n:
            Nl = round(n**0.5)
            Nb = round(n**0.5)**2-n+1
        else:
            Nl = n**0.5
            Nb = 1
    elif round(n**0.5)**2%2!=0:
        if round(n**0.5)**2<n:
            Nb = round(n**0.5)+1
            Nl = n-round(n**0.5)**2
        elif round(n**0.5)**2>n:
            Nb = round(n**0.5)
            Nl = round(n**0.5)**2-n+1
        else:
            Nb = n**0.5
            Nl = 1

        

    motv = [str(Nl),str(int(Nb))]

    print(i,motv, end='')
    print("--- %s seconds ---" % (time.time() - start_time),end='')
    print(True if motv == otv else False, otv)