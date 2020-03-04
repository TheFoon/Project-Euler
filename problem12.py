def fact(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors
tri = 0
add = 1
while True:
    tri += add
    add += 1
    if len(fact(tri)) > 500:
        break
print(tri) # ötlet: primekre felosztani; azok alapján kiszámolni az osztók számát