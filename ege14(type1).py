for x in '0123456789ABCDEFGHIJKL':
    x1 = int(f'A23{x}AC0' , 22)
    x2 = int(f'GB{x}21670' , 22)
    if (x1 + x2) % 21 == 0:
        print(x, (x1 + x2) // 22)
