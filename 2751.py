import sys
n = int(input())

li = []
for i in range(n):
    a = int(int(sys.stdin.readline()))
    li.append(a)
li.sort()
for i in range(n):
    print(li[i])