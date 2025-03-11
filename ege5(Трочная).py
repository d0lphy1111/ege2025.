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
        b = '1' + b + '01'
    else:
        b = b + c(N % 3 * 4)
    return int(b,3)
print(max(N for N in range(1,10000) if f(N) < 199))

