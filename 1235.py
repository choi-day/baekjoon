n = int(input())
numList = []

for i in range(n):
    numList.append(input())

l = len(numList[0])

for i in range(1, l+1):
    newList = []
    for j in numList:
        newList.append(j[l-i:l])
    newSet = set(newList)
    if len(newList) == len(newSet):
        print(i)
        break