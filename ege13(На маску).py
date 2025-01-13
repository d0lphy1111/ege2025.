from ipaddress import *

for m in range(16,33):
    net = ip_network(f'143.131.211.37/{m}', 0)
    k = 0
    for ip in net:
        if f'{ip:b}'.count('1') == 10:
            k += 1
    if k == 15:
        print(m)