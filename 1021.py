import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))
d = deque(list(range(1, n+1)))
count = 0

for i in li:
    if(i ==  d[0]):
        d.popleft()
    else:
        r = d.index(i)
        l = len(d) - d.index(i)
        if(r > l):
           d.rotate(l)
           d.popleft()
           count += l
        else:
            d.rotate(-r)
            d.popleft()
            count += r
print(count)
