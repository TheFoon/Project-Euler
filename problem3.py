import time
time1 = time.time()
num = 600851475143
factors = []
while True:
    if num == 1:
        break
    f = 2
    while True:
        if num % f == 0:
            factors.append(f)
            num = num / f
            break
        f += 1
print(factors[-1])
time2 =  time.time()
print(time2-time1)