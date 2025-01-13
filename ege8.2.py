from itertools import product, repeat

a = list(product('0123456789ab', repeat=5))

for x in a:
    x = ''.join(x)
