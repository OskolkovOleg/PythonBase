r = int(input())
c = int(input())
k = int(input())
flag = True
if c == 1:
    if r - k == 1:
        flag = False        
    else: 
        h = [[ 'U' for j in range(c)] for i in range(k)] + [[ 'D' for j in range(c)] for i in range(r - k - 1)] + [[ 'U' for j in range(c)] for i in range(1)]  
    
else:
    h = [[ 'R' for j in range(c)] for i in range(r)]  
    cnt = 0
   
    for i in range(r):
        if i % 2 == 0:
            for j in range(c):
                if cnt < k:
                    h[i][j] = 'L'
                    if j == 0 and i > 0:
                        h[i][j] = 'U'
                    cnt += 1
                else:
                    h[i][j] = 'R'
                    if j == c - 1:
                        if cnt > k:
                            h[i][j] = 'L'
                        elif i < r - 1:
                            h[i][j] = 'D'
                        else:
                            flag = False
                            break
                    cnt += 1
        else:
            for j in range(c - 1, -1, -1):
                if cnt < k:
                    h[i][j] = 'R'
                    if j == c - 1:
                        h[i][j] = 'U'
                    cnt += 1                    
                else:
                    h[i][j] = 'L'
                    if j == 0:
                        if cnt > k:
                            h[i][j] = 'R'
                        elif i < r - 1:
                            h[i][j] = 'D'
                        else:
                            flag = False
                            break                        
                    cnt += 1
if not flag:
    print('IMPOSSIBLE')
else:
    for i in range(r):
        for j in range(c):
            print(h[i][j], end = '')
        print()
