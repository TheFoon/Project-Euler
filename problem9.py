a = 1 # 342031st person to have solved this problem
while a < 1000:
    b = a
    while True:
        b += 1
        if a + b < 1000:
            c = 1000-a-b
            if a**2 + b**2 == c**2:
                print(a, b, c, a*b*c)
        else:
            a += 1
            break