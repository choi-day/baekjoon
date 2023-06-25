import sys
from collections import deque

n = int(input())

if(n == 0): print(0)

li = []

for _ in range(n):
    i = int(sys.stdin.readline().strip())
    li.append(i)

d = deque(sorted(li))
count = round(n * 0.3)

for _ in range(count):
    d.popleft()
    d.pop()

print(round(sum(d)/len(d)))