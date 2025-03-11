def f(x):
    div = set()
    for m in range(1, int(x ** 0.5) + 1):
        if x % m == 0:
            div.add(m)
            div.add(x // m)
    return sorted(div)[-2]
def g(x):
    div = set()
    for m in range(1, int(x ** 0.5) + 1):
        if x % m == 0:
            div.add(m)
            div.add(x // m)
    return sorted(div)[1]

def m(x):
    x1 = f(x)
    x2 = g(x)
    x3 = x1 - x2
    return x3

for x in range(850000,900000):
    a = m(x)
    if a % 13 == 0:
        if a > 0:
            print(x,a)

