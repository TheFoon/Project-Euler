from problem3 import fact
d = {}
d_t = {}
for i in range(1, 21):
    d_t = {}
    for f in fact(i):
        if f in d_t:
            d_t[f] += 1
        else:
            d_t[f] = 1
    for key in d_t:
        if key in d:
            d[key] = max(d[key], d_t[key])
        else:
            d[key] = d_t[key]
result = 1
for key in d:
    result *= key**d[key]
print(result)