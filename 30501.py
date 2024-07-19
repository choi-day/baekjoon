import sys
input = sys.stdin.readline

n = int(input())
nameList = []
for _ in range(n):
    nameList.append(input().strip())

for i in nameList:
    if 'S' in i:
        print(i)
        break