result = 0
l = [x for x in range(1000) if x % 3 == 0 or x % 5 == 0]
result = sum(l)
print(result)