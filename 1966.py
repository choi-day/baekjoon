import sys
from collections import deque

count = 0
a = int(input())

while(count != a):
    n, m = list(map(int, sys.stdin.readline().split(' ')))
    li = list(map(int, sys.stdin.readline().split(' ')))
    li = deque(li)
    c = 0
    hit = 0
    while(hit != 1):
        if(max(li) != li[0]):
            if(m != 0):
                k = li.popleft()
                li.append(k)
                m = m - 1
            else:
                k = li.popleft()
                li.append(k)
                m = len(li)-1
        else:
            if(m != 0):
                li.popleft()
                m = m - 1
                c = c + 1
            else:
                print(c+1)
                hit = hit +1
    count = count + 1