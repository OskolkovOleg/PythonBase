# 27820
def f(s, c, m):
    if s >= 42:
        return c % 2 == m % 2
    if c == m:
        return 0
    h = [f(s+1, c+1, m), f(s+2, c+1, m), f(s*2, c+1, m)]
    return any(h) if (c+1) % 2 == m % 2 else all(h)


for s in range(1, 42):
    for m in range(1, 6):
        if f(s, 0, m) == 1:
            if m == 2:
                print(s, m)
            break
