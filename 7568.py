n = int(input())
weight = list(range(n))
hight = list(range(n))
rank = list(1 for i in range(n))

for i in range(n):
    weight[i], hight[i] = list(map(int, input().split(' ')))
for i in range(n):
    for j in range(n):
        if((weight[i] < weight[j]) & (hight[i] < hight[j])) :
            rank[i] = rank[i]+1
print(*rank)