def f(N):
    b = bin(N) [2:]
    if N % 2 == 0:
        b = b + '10'
    else:
        b = '1' + b + '01'
    return int(b,2)
print(max([f(N) for N in range(0,200) if N <= 12]))

print('lox')