from ipaddress import *
net = ip_network('192.168.248.176/255.255.255.240', 0)
k = 0
for ip in net:
    if f'{ip:b}'.count('1') == f'{ip:b}'.count('0'):
        k += 1
print(k)