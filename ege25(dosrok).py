def f(x):
    div = set()
    for m in range(2, int(x ** 0.5) + 1):
        if x % m == 0:
            div.add(m)
            div.add(x // m)
    return sorted(div)

for x in range(1125000, 1126000):
    d = [i for i in f(x) if i % 10 == 7 and i != 7]
    if len(d) > 0:
        print(d, x)

