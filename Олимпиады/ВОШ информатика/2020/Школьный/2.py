import time
start_time = time.time()

for i in range(1,10):
    with open(f'archive_9-11/2/tests/0{i}', 'r') as f:
        #s =int(f.readline().strip())
        A =int(f.readline().strip())
        B =int(f.readline().strip())
        #p = [int(f.readline().strip()) for i in range(N)]
    with open(f'archive_9-11/2/tests/0{i}.a', 'r') as f2:
        otv = f2.readline()
    start_time = time.time()
   
    motv = 0
    motv1,motv2 = 0,0
    if A==0 and B==0:
        print(f'{i}:',0,0, end='')
    
        # while k!=0:
        #     if A==B:
        #         motv1+=k//2
        #         motv2+=k//2
        #         A=0
        #         B=0
        #         k=0
        #     elif A>B:
        #         k-=1
        #         motv1+=1
        #         A-=2
        #         B-=1
        #     else:
        #         k-=1
        #         motv2+=1
        #         A-=1
        #         B-=2
        # if A==B:
        #     motv1+=k//2
        #     motv2+=k//2
        # elif A>B:
        #     x = A%B
        #     A-=x//2*4
        #     B-=x//2*2
        #     k-=x//2*2
            
        #     motv1+=x//2*2
        #     x = B%A
        #     if x ==1:
        #         A-=2
        #         B-=1
        #         motv1+=1
        #         k-=1
        #     motv1+=k//2
        #     motv2+=k//2
        # elif A<B:
        #     x = B%A
        #     B-=x//2*4
        #     A-=x//2*2
        #     motv2+=x//2*2
        #     k-=x//2*2
        #     x = B%A
        #     if x ==1:
        #         B-=2
        #         A-=1
        #         motv2+=1
        #         k-=1
        #     motv2+=k//2
        #     motv1+=k//2
    if (A+B)%3!=0:
        print(-1)
    else:
        n = (A+B)//3
        if A>=n and B>= n:
            print(A-n, B-n)
        else:
            print(-1)



    
    print("--- %s seconds ---" % (time.time() - start_time),end='')
    print(otv)
    