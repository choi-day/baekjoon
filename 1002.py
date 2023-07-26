import sys
from math import sqrt
from decimal import Decimal

input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = sqrt(((x1-x2)**2) + ((y1-y2)**2))
    d = Decimal(d)
    if(r1 < r2):
        r1, r2 = r2, r1

    if(d > (r1+r2)): # 외부에서 만나지 않음
        print(0)
    elif(d == r1+r2): #외접
        print(1)
    elif(d > r1-r2 and d < r1+r2):
        print(2)
    elif(d == 0): 
        if(r1 == r2):
            print(-1)
        else:
            print(0)
    elif(d == r1-r2): #내접
        print(1)
    elif(d < r1-r2): # 내부에서 만나지 않음
        print(0)