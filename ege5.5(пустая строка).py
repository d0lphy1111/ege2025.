def c(N):
    b = ''
    if N == 0:
        return '0'

    while N > 0:
        b = str(N % 3) + b
        N //= 3
    return b


def f(N):
    b = c(N)
    if N % 3 == 0:
        b = b + b[-2:]
    else:
        b = b + c(b.count('1') + b.count('2'))
    return int(b, 3)

print(min(f(N) for N in range(0,1001,2) if f(N) > 220))