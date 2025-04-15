s = open('testege.txt').readline()
m = 0
for x in 'QWERTYUIOPSDFGHJKLZXCVNM':
    s = s.replace(x, ' ')
for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l:r+1]
        if ' ' not in c and c[0] != '0':
            if c[-1] == '2' or c[-1] == '4' or c[-1] == '6' or c[-1] == '8' or c[-1] == 'A':
                m = max(m,len(c))
        else:
            break
print(m)