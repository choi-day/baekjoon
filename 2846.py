n = int(input())
l = list(map(int, input().split()))

start = 0
finish = 0
best = 0

for i in range(1, n):
    if l[i] > l[i-1]:
        finish = i
        if best < l[finish] - l[start]:
            best = l[finish] - l[start]
    else:
        start = i
        finish = i
print(best)