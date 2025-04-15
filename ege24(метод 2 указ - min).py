s = open('testege.txt').readline()
l = 0
k = 0
m = 100000
for r in range(len(s)):
    if s[r] == 'Y':
        l = r + 1
        k = 0

    if s[r] == 'X': k += 1
    while k >= 500:
        if s[l] == 'X': k -= 1
        m = min(m, r - l + 1)
        l += 1
print(m)