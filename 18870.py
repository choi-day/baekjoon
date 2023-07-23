import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

setList = sorted(list(set(li)))

dic = {setList[i] : i for i in range(len(setList))}
for i in li:
    print(dic[i], end = ' ')