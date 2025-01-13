from ipaddress import *
for A in range(256):
    net = ip_network(f'192.214.{A}.184/255.255.255.224', 0)
    adr = ip_address(f'192.214.{A}.184')
    if adr not in [net[0], net[-1]]:
        if all(f'{ip:b}'.count('1') > 15 for ip in net):
            print(A)
            break