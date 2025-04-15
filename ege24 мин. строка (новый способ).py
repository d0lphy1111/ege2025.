s = open('testege.txt').readline()
m = 100000
for l in range(len(s)):
    for r in range(l, l + m):
        c = s[l:r+1]
        if c.count('AB') == 21:
            m = min(m, len(c))
            break
print(m)