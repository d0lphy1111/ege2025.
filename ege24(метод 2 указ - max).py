s = open('testege').readline()
k = 0
l = 0
m = 0
for r in range(len(s)):
    if s[r - 1] + s[r] == 'AB': k += 1
    while k > 100:
        if s[l] + s[l + 1] == 'AB': k -= 1
        l += 1
    if k == 100: m = max(m, r - l + 1)
print(m)
