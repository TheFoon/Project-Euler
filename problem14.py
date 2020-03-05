def Collatz_Length(n):#216453rd person to have solved this problem
    number = n
    length = 1
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1
        length += 1
    return length
max_length = -1
max_starter = -1
print(Collatz_Length(0))
for i in range(1, 10**6):
    l = Collatz_Length(i)
    if l > max_length:
        max_length = l
        max_starter = i
print(max_length)
print(max_starter)#837799