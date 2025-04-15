from re import *
s = open('testege.txt').readline()

reg = r'([1-9][0-9]*|0)'

reg = rf'({reg}([*+]{reg})*)'

reg = rf'(?=({reg}))'


m = max([x.group(1) for x in finditer(reg,s)], key = len)

print(m, len(m))



