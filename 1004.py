#20230814
#시작점이나 도착점이 원 안에 있으면 무조건 원을 뚫고 지나가야 하므로
#시작점이나 도착점이 각 원 안에 있는가 없는가를 확인하면 된다고 생각
#시작점과 도착점이 모두 한 원 안에 있는 것을 생각하지 못하여 한 번 틀림 

import sys
from math import sqrt
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    circle = []
    count = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input().rstrip())
    for _ in range(n):
        a, b, r = map(int, input().split())
        circle.append((a,b,r))
    for cir in circle:
        startd = sqrt((x1-cir[0])**2+(y1-cir[1])**2)
        arrivd = sqrt((x2-cir[0])**2+(y2-cir[1])**2)
        if(startd < cir[2] and arrivd < cir[2]):
            continue
        if(startd < cir[2]):
            count += 1
        if(arrivd < cir[2]):
            count += 1
    print(count)