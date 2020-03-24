def d(n):#139490th
    return sum([x for x in range(1, n) if n % x == 0])
amicable_pairs = []
for i in range(1,10000):
    j = d(i)
    if d(j) == i and i != j:
        if i not in amicable_pairs:
            amicable_pairs.append(i)
        if j not in amicable_pairs:
            amicable_pairs.append(j)
print(sum(amicable_pairs))#31626