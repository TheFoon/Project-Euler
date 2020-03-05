from problem3 import fact as f#210673rd person to have solved this problem
def fact(n):
    d = {}
    p_factors = f(n)
    for i in p_factors:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    factors = 1
    for i in d:
        factors *= d[i] + 1
    return factors
tri = 0
add = 1
while True:
    tri += add
    add += 1
    if fact(tri) > 500:
        break
print(tri)#76576500