def f(x,y,A):
    return (x - 3 * y < A) or (y > 400) or (x > 56)

print(min(A for A in range(0, 200) if all (f(x,y,A) == 1 for x in range(1, 200) for y in range(1,200))))