import sys
input = sys.stdin.readline

while(1):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    c = a * 3 - b - a
    print(c)