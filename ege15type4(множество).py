k = 0
for x in [k * 0.25 for k in range(-10000,10000)]:
    P = x in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    Q = x in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    A = 1
    f = (A <= P) and ((not Q) <= (not A))
    if f != 0:
        k += 1
print(k)

