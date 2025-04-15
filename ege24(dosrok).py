from re import *
s = open('testege.txt').readline()

reg = r'[1-9AB][0-9AB]*[02468A]|0'

reg = rf'(?=({reg}))'

print(max(len(x.group(1)) for x in finditer(reg,s)))
