for n in range(1, 10000, 2):
    b = bin(n)[2:]
    if n % 5 ==0:
        b = b[:3] + b
    else:
        b = b + bin((n % 5)*5)[2:]
    r = int(b,2)
    if r < 313:
        print(n)
