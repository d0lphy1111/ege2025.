print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (((x and not(y)) <= (z and w)) and ((y <= z) or (w <= x)))==0:
                    print(x,y,w,z)
