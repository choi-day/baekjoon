import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    k = int(input())
    num = list(map(int, input().split()))
    n = int(input())
    count = 0
    bestTime = 10000
    bestNo = 0
    for j in range(n):
        no, h, m = map(int, input().split())
        if no in num:
            if (h < 6 and h != -1) or (h == 6 and m == 0):
                count += 1
                if h * 60 + m < bestTime:
                    bestTime = h * 60 + m
                    bestNo = no
        else:
            pass
    print(bestNo, count)