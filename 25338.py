import sys
input = sys.stdin.readline

a,b,c,d = map(int, input().split())
n = int(input())
count = 0
for _ in range(n):
    u, v = map(int, input().split())
    if max(a*(v-b)**2+c,d) == u:
        count+=1
print(count)