for a in range(1,10):
    aa = (10*a) + a
    for b in range(1,10):
        bb = (10*b) +b
        res = aa * bb
        c1 = res // 1000
        reste = res % 1000
        c2 = reste // 100
        reste = reste % 100
        if c1 == c2:
            d1 = reste // 10
            d2 = reste % 10
            if d1 == d2:
                print(aa," * ",bb," = ",res)
