n = list(input())
a = []

for i in n:
    a.append(i)

a = reversed(sorted(a))
print(''.join(a))