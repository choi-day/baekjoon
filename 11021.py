import sys
input = sys.stdin.readline
count = 1

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print('Case #'+str(count)+':', a+b)
    count += 1