import sys

n = int(sys.stdin.readline().strip())
li = sorted(list(map(int,sys.stdin.readline().strip().split(' '))))

s = 0
for i in range(n):
    s += li[i]*(n-i)
print(s)