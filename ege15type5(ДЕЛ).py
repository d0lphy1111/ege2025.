def f(x,A):
    return (x % 7 != 0 or x % 13 ==0) <= (x > A - 40)
print(max(A for A in range(1,200) if all(f(x,A) == 1 for x in range(1,2000))))