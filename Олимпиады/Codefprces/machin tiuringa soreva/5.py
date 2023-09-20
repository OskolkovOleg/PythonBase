a = ["beer", "bear","type", "deer", "hair"]

for i in a:
    s = 0
    for j in i:
        s += ord(j)
    print(s)
