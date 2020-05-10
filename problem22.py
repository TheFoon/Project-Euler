with open('p022_names.txt') as f:#871198282
    names = f.read().strip('"').split('","')
names.sort()
s = 0
for i, name in enumerate(names):
    s += (i + 1) * sum([ord(x) - 64 for x in name])
print(s)#You are the 129853rd person to have solved this problem.