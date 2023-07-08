import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    m = int(sys.stdin.readline().strip())
    close = {}
    ca = []
    num = [1 for i in range(m)]
    j = 0
    for _ in range(m):
        a, b = sys.stdin.readline().strip().split(' ')
        if(b not in ca):
            ca.append(b)
        num[ca.index(b)] += 1
    sum = 1
    for i in num:
        if(i != 1):
            sum *= i
    print(sum-1)