clustersA = [[], []]
clustersB = [[], [], []]

for line in open('27a.txt'):
    x,y = [float(x) for x in line.split()]
    if y < 3:
        clustersA[0].append([x,y])
    else:
        clustersA[1].append([x,y])

for line in open('27b.txt'):
    x,y = [float(x) for x in line.split()]
    if y < 3:
        clustersB[0].append([x,y])
    if y > 3 and y < 7:
        clustersB[1].append([x,y])
    if y > 7:
        clustersB[2].append([x,y])

def d(A,B):
    x1, y1 = A
    x2, y2 = B
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def center(cl):
    m = []
    for p in cl:
        sm = sum(d(p,p1) for p1 in cl)
        m.append([sm,p])
    return min(m)[1]

centersA = [center(cl) for cl in clustersA]
centersB = [center(cl) for cl in clustersB]
pxA = int(sum(x for x,y in centersA) / 2 * 10000)
pyA = int(sum(y for x,y in centersA) / 2 * 10000)
pxB = int(sum(x for x,y in centersB) / 3 * 10000)
pyB = int(sum(y for x,y in centersB) / 3 * 10000)
print(pxA,pyA)
print(pxB,pyB)
