n = int(input())
arr = [list(input()) for i in range(n)]

ic = []
for i in arr:
    if not ("#" in i):
        ic.append(i)
    else:
        break
for i in arr[::-1]:
    if not ("#" in i):
        ic.append(i)
    else:
        break
for i in ic:
    arr.remove(i)

def bar(index, arr):
    return [i[index] for i in arr]
k = 0
for j in range(len(arr[0])):
    c = bar(j, arr)
    if not "#" in c:
        k+=1
    else:
        break

for i in range(len(arr)):
    arr[i] = arr[i][k:]
for i in range(len(arr[0])-1,0,-1):
    
    c = bar(i, arr)
    if not "#" in c:
        for i in range(len(arr)):
            arr[i] = arr[i][:-1]
    else:
        break
flag1 = True
flag2 = False
flag3 = False
flag4 = False
flag5 = False
flag6 = False
for i in range(len(arr)-1):
    if not (arr[i] == arr[i+1] and flag1 and (not '.' in arr[i])):
        flag1 = False
if arr[0] == arr[-1] and not '.' in bar(0, arr):
    if '.' in arr[0] \
            and (not '.' in bar(0, arr)) \
            and (not '.' in bar(-1, arr)):
        for i in arr:
            if not '.' in i:
                flag5 = True
    elif bar(0, arr) == bar(-1, arr) :
        flag2 = True
        for i in range(1,len(arr)-2):
            if arr[i] == arr[i+1] or not flag2:
                flag2 = True
            else:
                flag2 = False
    else:
        flag3 = True
        for i in range(1,len(arr)-2):
            if arr[i] == arr[i+1] or not flag3:
                flag3 = True
            else:
                flag3 = False
else:
    if not '.' in bar(0, arr) and not '.' in arr[-1]:
        flag4 = True
        for i in range(len(arr)-2):
            if arr[i] == arr[i+1] or not flag4:
                flag4 = True
            else:
                flag4 = False 
    elif not '.' in bar(0, arr) \
            and not '.#' in bar(-1, arr) \
            and not '.' in arr[0] \
            and arr[0] in arr[1:]:
        flag6 = True
if flag1:
    motv = 'I'
elif flag2:
    motv = 'O'
elif flag3:
    motv = 'C'
elif flag4:
    motv = 'L'
elif flag5:
    motv = 'H'
elif flag6:
    motv = 'P'
else:
    motv = 'X'

print(motv)