for x in [k * 0.25 for k in range(-10000,10000)]:
    C = 48 <= x <= 94
    J = 83 <= x <= 100
    A = 1
    f = not(C or J) <= (not A)
    if f != 0:
        print(x)