s = open('testege.txt').readline()
m = 0
for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l:r+1]
        if 'PR' not in c and 'RP' not in c:
            m = max(m, len(c))
        else:
            break
print(m)