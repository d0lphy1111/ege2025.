for n in range (1,10000):
    b = bin(n)[2:]
    if b.count('1') % 2 ==0:
        b = b + '11'
    else:
        b = b +'01'
    r = int(b,2)
    if r > 61:
        print(r)
        break