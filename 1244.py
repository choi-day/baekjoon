import sys
input = sys.stdin.readline

n = int(input().strip())
nList = list(input().split())
stdNum = int(input())

def changeNum(n):
    global nList
    if nList[n] == '0':
        nList[n] = '1'
    else:
        nList[n] = '0'

for i in range(stdNum):
    s, getNum = map(int,input().split())
    if s == 1:
        for j in range(getNum, n+1, getNum):
            changeNum(j-1)
    else:
        changeNum(getNum-1)
        k = 1
        while(getNum-1-k > -1 and getNum-1+k < len(nList)):
            if(nList[getNum-1-k] == nList[getNum-1+k]):
                changeNum(getNum-1-k)
                changeNum(getNum-1+k)
                k+=1
            else:
                break
for i in range(0, n, 20):
    print(' '.join(nList[i:i+20]))