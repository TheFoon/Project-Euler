def fact(x):#189977th person to have solved this problem
    if x == 1:
        return 1
    return x * fact(x-1)
print(sum([int(x) for x in str(fact(100))]))#648