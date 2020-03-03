def prime(n):#312828th person to have solved this problem
    primes = [2, 3, 5]
    p = 7
    while p < n:
        for i in primes:
            if p % i == 0:
                break
        else:
            primes.append(p)
        p += 2
    return primes
print(sum(prime(2000000)))#142913828922