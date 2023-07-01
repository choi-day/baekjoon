import sys
from collections import deque

n = int(input())
li = [int(sys.stdin.readline().strip()) for i in range(n)]
d = deque()
result = []

i = 1
while(len(li)!=0):
    if(i < li[0]):
        d.append(i)
        result.append('+')
        i = i + 1

    elif(i == li[0]):
        d.append(i)
        result.append('+')
        i = i + 1
        a = li.pop(0)
        b = d.pop()
        if(a != b): print('NO'); break
        result.append('-')

    else:
        a = li.pop(0)
        b = d.pop()
        if(a != b): print('NO'); break
        result.append('-')
if(len(li) == 0):
    print(*result, sep='\n')