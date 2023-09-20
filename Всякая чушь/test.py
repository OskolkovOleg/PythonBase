
s = []
for i in range(55_296):
    s.append(chr(i))

with open("1.txt", "w", encoding="utf") as f:
    f.write("".join(s))
                
