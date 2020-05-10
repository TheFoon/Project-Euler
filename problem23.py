import math#4179871
def get_divs(n) : 
    i = 2
    a = [1]
    while i <= math.sqrt(n): 
          
        if (n % i == 0) : 
               
            if (n / i == i) : 
                a.append(i)
            else :
                a.append(i)
                a.append(n/i)
        i = i + 1
    return a
def prop_divs(n):
    return [i for i in range(1, n) if n % i == 0]
def is_abundant(n):
    return sum(get_divs(n)) > n
def get_abundant(n):
    return [i for i in range(1, n) if is_abundant(i)]
lim = 28123
ab = get_abundant(lim)
print('Got Abundant Numbers!')
print(ab[:10])
s = 0
for i in range(1, lim + 1):
    if i % 100 == 0:
        print(f'{i} - {s}')
    for j in ab:
        if i > j:
            if is_abundant(i - j):
                break 
    else:
        s += i
print(s)#You are the 100278th person to have solved this problem.
