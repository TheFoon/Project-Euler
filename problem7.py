def prime(n):
    primes = [2, 3, 5]
    p = 7
    while len(primes) < n:
        for i in primes:
            if p % i == 0:
                break
        else:
            primes.append(p)
        p += 2
    return primes
print(prime(10001)[-1])        