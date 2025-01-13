def f(x,end):
    if x < end: return 0
    if x == end: return 1
    turns = []
    turns.append(f(x - 3, end))
    if x % 2 == 0:
        turns.append(f(x // 3, end))
    if x >= 10:
        turns.append(f(x // 10, end))
    return sum(turns)
print(f(1250,20))