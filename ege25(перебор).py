def f(x):
    div = set()
    for m in range(1, int(x ** 0.5) + 1):
        if x % m == 0:
            if m != x and m != 9 and m % 10 == 9:
                div.add(m)
            if (x // m) != x and (x // m) != 9 and (x // m) % 10 == 9:
                div.add(x // m)
    return div

for x in range(800001, 801000):
    div = f(x)
    if len(div) != 0:
        print(x, min(div))

