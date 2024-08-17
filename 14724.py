import sys
input = sys.stdin.readline

n = int(input())
l = [list(map(int, input().split()))for _ in range(9)]
group = ["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY"]

best = 0
count = 0
bestgroup = ''

for i in l:
    if best < max(i):
        best = max(i)
        bestgroup = group[count]
    count +=1

print(bestgroup)