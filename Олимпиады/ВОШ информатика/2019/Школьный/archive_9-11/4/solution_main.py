s = input()

i = 0
j = len(s) - 1
while i < j and s[i] == s[j]:
    i += 1
    j -= 1
if i >= j:
    print((len(s) + 1) // 2)
elif s[i:j] == s[i:j][::-1]:
    print(j + 1)
elif s[i + 1:j + 1] == s[i + 1:j + 1][::-1]:
    print(i + 1)
else:
    print(0)

