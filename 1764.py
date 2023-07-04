import sys

n, m=map(int, sys.stdin.readline().strip().split())
noListenList = {}
li = []

for i in range(n):
    a = sys.stdin.readline().strip()
    noListenList[a] = i
for i in range(m):
    a = sys.stdin.readline().strip()
    if(a in noListenList):
        li.append(a)
li = sorted(li)
print(len(li))
print(*li, sep='\n')