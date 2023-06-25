from collections import deque
import sys

input = sys.stdin.readline

while(1):
    a = input().rstrip()
    if(a == '.') : break
    d = deque()
    for i in a:
        if(i == '['):
            d.append(i)
        if(i == '('):
            d.append(i)    
        if(i == ']'):
            if(len(d) == 0): d.append(i); pass
            j = d.pop()
            if(j == '['): pass
            else: d.append(j); break
        if(i == ')'):
            if(len(d) == 0): d.append(i); pass
            j = d.pop()
            if(j == '('): pass
            else: d.append(j); break
    if(len(d)==0): print('yes')
    else: print('no')