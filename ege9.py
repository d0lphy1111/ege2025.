k = 0
for line in open('9.txt'):
    a = [int(x) for x in line.split()]
    p3 = [x for x in a if a.count(x)==3]
    p1 = [x for x in a if a.count(x)==1]
    if len(p3) == 3 and len(p1) == 3 and sum(p3)**2 > sum(p1)**2:
        k += 1
print(k)




