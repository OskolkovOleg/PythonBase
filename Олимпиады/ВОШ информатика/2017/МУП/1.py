# N
# K min натуральное число сумма цифр = N, K%N == 0
N = int(input())
for K in range(0, 1000000000, N):
    if K%N == 0 and sum([int(i) for i in str(K)]) == N:
        break
print(K)
