def f(N):
    b = bin(N) [2:]
    b = b + str(b.count('1') % 2)
    b = b + str(b.count('1') % 2)
    return int(b,2)
print(min(f(N) for N in range(0,1000) if f(N) > 75))