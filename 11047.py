import sys

n, k = map(int, sys.stdin.readline().strip().split())
v = []

for _ in range(n):
    a = int(sys.stdin.readline().strip())
    v.append(a)
coin = 0
i = len(v)-1
while(k!=0):
    if(v[i]>k):
        i -= 1
    else:
        coin += int(k/v[i])
        k -= v[i]*int(k/v[i])
        i -= 1
print(coin)