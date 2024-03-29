import sys
input = sys.stdin.readline
sNum = 0

while(1):
    sNum += 1
    n = int(input().strip())
    if n == 0:
        break
    numList = []
    nameList = []
    for i in range(n):
        nameList.append(input().strip())
    for i in range((n*2)-1):
        a = input().strip()
        if len(a) < 2:
            print(nameList[int(a)])
            break
        else:
            num, al = a.split()
            num = int(num)
        if num in numList:
            numList.remove(num)
        else:
            numList.append(num) 
    if len(numList) > 0:
        print(sNum, nameList[numList[0]-1])