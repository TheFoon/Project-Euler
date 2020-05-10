def isPalindrome(s):
    return str(s) == str(s)[::-1]
p = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if i*j > p and isPalindrome(i*j):
            p = i*j
print(p)