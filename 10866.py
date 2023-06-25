import sys
from collections import deque

n = int(input())
d = deque([])
count = 0

while(count!=n):
    cmd = sys.stdin.readline().strip()
    if(cmd.startswith('push_front')):
        m = []
        for i in cmd:
            if(i.isdigit()): m.append(i)
        m = ''.join(map(str, m))
        d.appendleft(int(m))
    if(cmd.startswith('push_back')):
        m = []
        for i in cmd:
            if(i.isdigit()): m.append(i)
        m = ''.join(map(str, m))
        d.append(int(m))
    if(cmd == 'pop_front'):
        if(len(d) == 0): print(-1)
        else: print(d.popleft())
    if(cmd == 'pop_back'):
        if(len(d) == 0): print(-1)
        else: print(d.pop())
    if(cmd == 'size'):
        print(len(d))
    if(cmd == 'empty'):
        if(len(d) == 0): print(1)
        else: print(0)
    if(cmd == 'front'):
        if(len(d) == 0): print(-1)
        else:
            f = d.popleft()
            print(f)
            d.appendleft(f)
    if(cmd == 'back'):
        if(len(d) == 0): print(-1)
        else:
            b = d.pop()
            print(b)
            d.append(b)
    count = count + 1