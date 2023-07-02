import sys
N, M, B = map(int,sys.stdin.readline().split())
block = []
for _ in range(N):
    block += list(map(int,sys.stdin.readline().split()))

hitTime= float('inf')
hitHight = 0
for i in range(min(block), max(block)+1):
    t = 0
    b = B
    for j in block:
        if(i > j):
            t = t + (i - j)
            b = b - (i - j)
        else:
            t = t + (j - i)*2
            b = b + (j - i)
    if(b < 0): continue
    if(hitTime > t):
        hitTime = t
        hitHight = i
    elif(hitTime == t):
        if(hitHight < i):
            hitHight = i
print(hitTime, hitHight)