a = [int(x) for x in open('testege')]
m = []
for i in range(len(a)):
    if (a[i] % 10 == 2 or a[i] % 10 == 7) and a[i] % 3 == 0 and a[i] % 11 == 0:
        m.append(a[i])
print(len(m),min(m))
