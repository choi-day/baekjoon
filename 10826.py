n = int(input())

l = [0, 1]

for  i in range(1, n):
    l.append(l[i-1] + l[i])

print(l[n])