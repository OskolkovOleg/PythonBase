import time
start_time = time.time()



for i in range(19,27):
    with open(f'archive-9-11/4/tests/{i}', 'r') as f:
        N =int(f.readline().strip())
        D =int(f.readline().strip())
        a = [int(f.readline().strip()) for i in range(N)]
        
    with open(f'archive-9-11/4/tests/{i}.a', 'r') as f2:
        otv = int(f2.readline().strip())
    start_time = time.time()

    # motv = 1
    # j = a[motv-1]
    # while D<=j:
    #     if j != a[-1]:
    #         k=2
    #         while D*k<=a[motv-3+k] and a[motv-3+k] != a[-k]:
    #             if a[motv-2+k]>=a[motv-3+k] :
    #                 k+=1
    #                 continue
    #             else:
    #                 motv+=k
    #                 break
                

    #         else:
    #             motv+=1
            
    #     else:
    #         break
    #     j = a[motv-1]
        
        

    
    motv = 1
    i = 1
    while i <= N and i <= motv:
        jump = int(input())
        motv = max(motv, i + jump // D)
        i += 1
    motv = min(motv, N)
    
 
 


    


    print(f'{i}:',motv, end='')
    print("--- %s seconds ---" % (time.time() - start_time),end='')
    print(True if motv == otv else False)