def p(x):
    return x > 1 and all(x % d != 0 for d in range(2, int(x ** 0.5) + 1))

def f(x):
    divs = set()
    for d in range(1, int(x ** 0.5) + 1):
        if x % d == 0:
            if p(d):
                divs.add(d)
            if p(x // d):
                divs.add(x // d)
    return divs

for x in range(1000000,1000500):
    divs = f(x)
    if len(divs) == 3:
        print(x, max(divs))