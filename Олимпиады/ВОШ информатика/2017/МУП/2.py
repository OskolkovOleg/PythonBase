line = input()
maximum = max(line)
if maximum in '0123456789':
    print(int(line, int(maximum)+1))
else:
    print(int(line, ord(max(line))-ord('A')+11))
