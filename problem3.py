import time
num = 600851475143

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print(f'{f.__name__:s} function took {(time2-time1)*1000.0:.3f} ms')
        return ret
    return wrap

def fact(n):
    number = n
    factors = []
    f = 2
    while True:
        if number == 1:
            break
        while True:
            if number % f == 0:
                factors.append(f)
                number = number / f
                break
            f += 1
    return factors

#print(fact(num)[-1])
@timing
def gut():
    for _ in range(100):
        fact(543864738953723849127423623532)
gut()