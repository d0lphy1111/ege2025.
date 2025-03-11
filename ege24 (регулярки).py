from re import *

s = open('testege').readline()

reg = r'[1-9][0-9]{3}\.[0-9]+&[1-9][0-9]{3}\.[0-9]+'

reg = rf'(?=({reg}))'

print(max(len(x.group(1)) for x in finditer(reg,s)))