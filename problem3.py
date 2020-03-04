num = 600851475143

def fact(n):
    number = n
    factors = []
    while True:
        if number == 1:
            break
        f = 2
        while True:
            if number % f == 0:
                factors.append(f)
                number = number / f
                break
            f += 1
    return factors

print(fact(num)[-1])