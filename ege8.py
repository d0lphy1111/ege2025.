from itertools import product

a = list(product('АГДИЛНРЯ', repeat=6))

n=0
for x in a:
    n +=1
    x =''.join(x)
    if n % 2 ==0 and x[0]!='Я' and x.count('Д')==3:
        print(n)