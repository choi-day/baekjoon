import sys
input = sys.stdin.readline

n , m = map(int, input().split())
coustomer =  []
for _ in range(m):
    coustomer.append(int(input()))
coustomer = sorted(coustomer)
if n < m:
    coustomer = coustomer[m-n-1:m]
profit = []

for i in coustomer:
    profit.append(i * len(coustomer[coustomer.index(i):m]))
bestPrice = coustomer[profit.index(max(profit))]

print(bestPrice ,max(profit))