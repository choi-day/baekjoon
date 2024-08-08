import sys
input = sys.stdin.readline

n, k = map(int, input().split())
l = [list(input().split()) for _ in range(n)]

for i in l:
    tmp = []
    for j in i:
        for m in range(k):
            tmp.append(j)
    for _ in range(k):
        print(' '.join(tmp))