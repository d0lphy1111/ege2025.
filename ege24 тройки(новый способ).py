s = open('testege.txt').readline()
for c in '123':
    s = s.replace(c, '0')
for f in 'ABC':
    s = s.replace(f, 'A')

m = 0
for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l:r+1]
        if len(c) % 3 == 0:
            if all(c[i] + c[i + 1] + c[i + 2] == '0A0' for i in range(0,len(c), 3)):
                m = max(m, len(c))
            else:
                break
print(m//3)