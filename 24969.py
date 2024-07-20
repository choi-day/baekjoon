import sys
input = sys.stdin.readline

n , k = map(int, input().strip().split())
numList = list(map(int, input().strip().split()))
count = 0

for last in range(n-1, 0, -1):
    for i in range(last):
        if numList[i]>numList[i+1]:
            count += 1
            numList[i], numList[i+1] = numList[i+1], numList[i]
        if count == k:
            print(*numList, sep=' ')
            sys.exit(0)
if count < k:
    print(-1)