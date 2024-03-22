import sys

input = sys.stdin.readline

groupNum = 0

while(1):
    groupNum += 1
    countN = 0
    n = int(input().strip())
    if n == 0:
        break
    arr = [list(input().split()) for _ in range(n)]
    if groupNum > 1:
        print('')
    print('Group', groupNum)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'N':
                countN += 1
                if i >= j:
                    print(arr[i-j][0],'was nasty about',arr[i][0])
                else:
                    print(arr[i-j+n][0],'was nasty about',arr[i][0])
    if countN == 0:
        print('Nobody was nasty')