from re import *

s = open('testege').readline()

reg = r'([1-9][0-9]*|0)'

reg = rf'(({reg}\*)*0(\*{reg})*)'

reg = rf'{reg}(\+{reg})+'

reg = rf'(?=({reg}))'

print(max(len(x.group(1)) for x in finditer(reg,s)))