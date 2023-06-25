import sys
from collections import deque

n = int(input())

def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

if(n == 0): print(0)
else:
    li = []

    for _ in range(n):
        i = int(sys.stdin.readline().strip())
        li.append(i)

    d = deque(sorted(li))
    count = round2(n * 0.15)

    for _ in range(count):
        d.popleft()
        d.pop()

    print(round2(sum(d)/len(d)))