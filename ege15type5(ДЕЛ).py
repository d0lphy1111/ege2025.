def f(x,y,A):
    return (x % A == 0) <= ((x % A == 0) <= (x % 34 == 0) and (x % 51 == 0))
print(min(A for A in range(1,200) if all (f(x,y,A) == 1 for x in range(1,200) for y in range(1,200))))