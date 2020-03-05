from problem3 import fact as f
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
    print(f"{tri}: {len(f(tri))} {len(fact(tri))}")
    if len(fact(tri)) > 50:
        break
print(tri) # ötlet: primekre felosztani; azok alapján kiszámolni az osztók számát