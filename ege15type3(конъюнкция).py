def f(x, A):
    return (x & 57 == 0) or ((x & 23 ==0) <= (not (x & A == 0)))

print(min(A for A in range(1,200) if all(f(x, A) == 1 for x in range(1,2000))))