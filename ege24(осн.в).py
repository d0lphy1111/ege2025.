s = open('testege.txt').readline()
while '++' in s: s = s.replace('++', '+ +')
while '**' in s: s = s.replace('**', '* *')
while '+*' in s: s = s.replace('+*', '+ *')
while '*+' in s: s = s.replace('*+', '* +')

m = []
for c in s.split(' '):
    for i in range(len(c) - 1):
        ps = c[i]
        if ps[0] not in '+*' and c[i] + c[i + 1] not in ['00','01','02','03','04','05','06','07','08','09']:
            for j in range(i + 1, len(c)):
                ps += c[j]
                if ps[-1] not in '+*':
                    if eval(ps) == 0:
                        m.append(len(ps))
print(max(m))