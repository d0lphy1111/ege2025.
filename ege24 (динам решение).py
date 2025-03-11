s = open('testege')
m = [0] * len(s)

for i in range(len(s)):
    if s[i] in 'ABCD':
        m[i] = m[i - 1] + 1
print(max(m))