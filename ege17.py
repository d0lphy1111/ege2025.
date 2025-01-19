a = [int(x) for x in open('17.txt')]
r = []
for i in range(len(a) - 1):
    if a[i] % 16 == min(a) or a[i + 1] % 16 == min(a):
        r.append(a[i] + a[i + 1])
print(len(r), max(r))