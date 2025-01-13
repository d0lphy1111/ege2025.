def f(N):
    n = bin(N)[2:]
    if len(n) % 2 == 0:
        n += '1'
    else:
        n = '1' + n + '0'
    return int(n, 2)
print(min([f(N) for N in range(1,10000) if f(N) > 666]))
