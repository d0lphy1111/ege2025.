def f(N):
    n = bin(N)[2:]

    if N % 3 == 0:
        n = '1' + n
        n = n[:-2] + '11'
    else:
        n = '10' + n + '0'

    return int(n, 2)



print(min([f(N) for N in range(2, 10000, 2) if f(N) > 999]))
