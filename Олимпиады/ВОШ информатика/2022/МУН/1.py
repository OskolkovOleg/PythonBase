a, b = map(int, input().split(' '))
arr1 = list(map(int, input().split(' ')))
arr2 = list(map(int, input().split(' ')))

arr3 = list(set([i for i in arr1 if i in arr2]))
print(len(arr3))
print(str(sorted(arr3))[1:-1].replace(',',''))
