N, M = map(int, (input(), input()))

max_vals = 0
count = 0

for x in range(N+1):
    for y in range(M+1):
        lenx = min(N - x, x)
        leny = min(y, M - y)
        # print(f'[{lenx, leny}]', end=' ')
        if (now_vals := (lenx + leny) / 2) > max_vals:
            max_vals = now_vals
            count = 1
        elif now_vals == max_vals:
            count += 1
# print()
print(count)