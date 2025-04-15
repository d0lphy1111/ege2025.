def f(x):
    return (x % a == 0) or (60 <= x <= 80) <= (x % 22 != 0)

for a in range(1,1000):
    if all(f(x) for x in range(1,2000)):
        print(a)