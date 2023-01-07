# 일단 정확한 알고리즘

len, max = map(int,input().split())
num = list(map(int, input().split()))
bingo = 0

from itertools import combinations

for i in combinations(num, 3):
    if(sum(i)<=max and sum(i)>bingo):
        bingo = sum(i)

print(bingo)