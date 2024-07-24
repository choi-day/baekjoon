import sys
input = sys.stdin.readline

t = int(input())
alpaList = [chr(x) for x in range(65, 91)]

for _ in range(t):
    test = input().strip()
    notInList = []
    for i in alpaList:
        if i not in test:
            notInList.append(ord(i))
    print(sum(notInList))