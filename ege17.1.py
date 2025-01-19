a = [int(x) for x in open('17.txt1')]
m = []
b = max(x for x in a if abs(x) % 10 == 3 and 100 <= abs(x) <= 999)
for i in range(len(a) - 2):
    m1 = (abs(a[i]) % 10 == 3 and 99 <= abs(a[i]) <= 999)
    m2 = (abs(a[i + 1]) % 10 == 3 and 99 <= abs(a[i + 1]) <= 999)
    m3 = (abs(a[i + 2]) % 10 == 3 and 99 <= abs(a[i + 2]) <= 999)
    if m1 + m2 + m3 >= 1:
        if a[i] + a[i + 1] + a[i + 2] < b:
            m.append(a[i] + a[i + 1] + a[i + 2])
print(len(m), max(m))